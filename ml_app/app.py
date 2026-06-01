import os
import asyncio
import json
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from datetime import datetime
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from typing import Optional

load_dotenv()

app = FastAPI(title="GenAI Agentic Service", description="Gemini API with agentic endpoints")

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

class SummarizeRequest(BaseModel):
    text: str
    max_sentences: Optional[int] = Field(3, ge=1, le=10)

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

async def call_gemini(prompt: str) -> str:
    """Helper to call Gemini API and return text response."""
    token = creds.token
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    response = await client.post(url, headers=headers, json=payload, timeout=30.0)
    response.raise_for_status()
    result = response.json()
    if result.get("candidates"):
        return result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        raise ValueError("No candidates in Gemini response")

@app.get("/")
async def home():
    return {
        "message": "Agentic GenAI Service",
        "endpoints": [
            "/health",
            "/llm-query/{query}",
            "/agent/summarize/{text}",
            "/agent/classify - POST with JSON"
        ]
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/llm-query/{query}")
async def get_llm_query(query: str):
    start_time = datetime.utcnow()
    status = "success"
    error_msg = None
    response_preview = None
    try:
        text = await call_gemini(query)
        response_preview = text[:200] + "..." if len(text) > 200 else text
        return {"response": text}
    except httpx.HTTPStatusError as e:
        status = "http_error"
        error_msg = f"HTTP error: {e.response.text}"
        print(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=error_msg)
    except Exception as e:
        status = "exception"
        error_msg = str(e)
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=error_msg)
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

# ---------- Agentic Endpoints ----------

@app.get("/agent/summarize/{text}")
async def agent_summarize(text: str, sentences: int = 3):
    """Agentic endpoint: summarize any text using Gemini."""
    if len(text) > 3000:
        text = text[:3000] + "..."
    prompt = f"Summarize the following text in exactly {sentences} sentences:\n\n{text}"
    try:
        summary = await call_gemini(prompt)
        return {"original_length": len(text), "summary": summary, "sentences": sentences}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/agent/classify")
async def agent_classify(request: QueryRequest):
    """Agentic endpoint: classify user query into categories (tech, science, general, etc.)"""
    prompt = f"""Classify the following user query into one of these categories: 
    ['technology', 'science', 'business', 'health', 'general', 'other'].
    Return ONLY the category name as a single word, nothing else.
    
    Query: {request.query}"""
    try:
        category = await call_gemini(prompt)
        # Sanitize output
        category = category.strip().lower().replace('.', '')
        if category not in ['technology', 'science', 'business', 'health', 'general', 'other']:
            category = 'general'
        return {"query": request.query, "category": category}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))