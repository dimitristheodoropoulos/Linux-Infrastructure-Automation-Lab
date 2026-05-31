import os
import asyncio
import json
import httpx
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from datetime import datetime
from google.oauth2 import service_account
from google.auth.transport.requests import Request

load_dotenv()

app = FastAPI()

# Service account authentication
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if not credentials_path:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS environment variable not set.")

SCOPES = ["https://www.googleapis.com/auth/generative-language"]
creds = service_account.Credentials.from_service_account_file(
    credentials_path, scopes=SCOPES
)
if not creds.valid:
    creds.refresh(Request())

# Logstash configuration
LOGSTASH_HOST = os.getenv("LOGSTASH_HOST", "localhost")
LOGSTASH_PORT = int(os.getenv("LOGSTASH_PORT", "5000"))

client = httpx.AsyncClient()

class QueryRequest(BaseModel):
    query: str

async def send_log_to_logstash(log_data: dict):
    try:
        if "timestamp" not in log_data:
            log_data["timestamp"] = datetime.utcnow().isoformat()
        message = json.dumps(log_data) + "\n"
        reader, writer = await asyncio.open_connection(LOGSTASH_HOST, LOGSTASH_PORT)
        writer.write(message.encode())
        await writer.drain()
        writer.close()
        await writer.wait_closed()
    except Exception as e:
        print(f"Failed to send log to Logstash: {e}", flush=True)

@app.get("/")
async def home():
    return {"message": "ML App is running! Use /llm-query/{query} to talk to Gemini."}

@app.get("/health")
async def health():
    """Health check endpoint for Kubernetes probes"""
    return {"status": "healthy"}

@app.get("/llm-query/{query}")
async def get_llm_query(query: str):
    start_time = datetime.utcnow()
    status = "success"
    error_msg = None
    response_preview = None

    try:
        token = creds.token
        # ✅ Stable model (not preview)
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        payload = {
            "contents": [{"parts": [{"text": query}]}]
        }

        response = await client.post(url, headers=headers, json=payload, timeout=30.0)
        response.raise_for_status()
        result = response.json()

        if result.get("candidates"):
            text = result["candidates"][0]["content"]["parts"][0]["text"]
            response_preview = text[:200] + "..." if len(text) > 200 else text
            return {"response": text}
        else:
            status = "error"
            error_msg = "Unexpected response format"
            return {"error": error_msg, "api_response": result}, 500

    except httpx.HTTPStatusError as e:
        status = "http_error"
        error_msg = f"HTTP error: {e.response.text}"
        print(f"HTTP error calling Gemini API: {e}")
        return {"error": error_msg}, e.response.status_code
    except Exception as e:
        status = "exception"
        error_msg = str(e)
        print(f"An unexpected error occurred: {e}")
        return {"error": error_msg}, 500
    finally:
        duration_ms = (datetime.utcnow() - start_time).total_seconds() * 1000
        log_entry = {
            "service": "ml-app",
            "endpoint": "/llm-query",
            "query": query,
            "status": status,
            "duration_ms": round(duration_ms, 2),
        }
        if error_msg:
            log_entry["error"] = error_msg
        if response_preview:
            log_entry["response_preview"] = response_preview
        asyncio.create_task(send_log_to_logstash(log_entry))