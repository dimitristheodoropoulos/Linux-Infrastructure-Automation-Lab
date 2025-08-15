# /home/testuser/Linux-Infrastructure-Automation-Lab/ml_app/app.py
import os
import httpx
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create the FastAPI application instance
app = FastAPI()

# Get the Google API key from the environment variable
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    # This will cause the container to fail on startup if the key is not set,
    # which is a good way to debug deployment issues.
    raise ValueError("GOOGLE_API_KEY environment variable not set.")

# Initialize the HTTP client for making API calls
client = httpx.AsyncClient()

# A simple Pydantic model for the request body
class QueryRequest(BaseModel):
    query: str

@app.get("/")
async def home():
    """A simple home page to confirm the app is running."""
    return {"message": "ML App is running! Use the /llm-query/YOUR_QUERY_HERE endpoint to get a response from the Gemini LLM."}

@app.get("/llm-query/{query}")
async def get_llm_query(query: str):
    """
    Sends a query to the Gemini LLM with a text query and returns the generated text.
    """
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key={api_key}"
        
        # Prepare the request payload
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {"text": query}
                    ]
                }
            ]
        }
        
        headers = {
            "Content-Type": "application/json"
        }
        
        # Make the asynchronous API call
        response = await client.post(url, headers=headers, json=payload, timeout=30.0)
        response.raise_for_status()
        
        result = response.json()
        
        if result.get("candidates"):
            text = result["candidates"][0]["content"]["parts"][0]["text"]
            return {"response": text}
        else:
            return {"error": "Unexpected response format from Gemini API.", "api_response": result}, 500
            
    except httpx.HTTPStatusError as e:
        print(f"HTTP error calling Gemini API: {e}")
        return {"error": f"HTTP error: {e.response.text}"}, e.response.status_code
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {"error": str(e)}, 500
