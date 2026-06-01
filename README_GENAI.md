# GenAI Agentic Service with Streamlit Frontend

This branch (`genai-agentic`) extends the base project with **agentic GenAI capabilities** using Google Gemini API.

## ✨ New Features

- **Agentic Endpoints**:
  - `/agent/summarize/{text}` – Summarizes any text in 2-3 sentences.
  - `/agent/classify` – Classifies user query into categories (technology, science, business, health, general, other).
- **Streamlit Frontend** (`dashboard.py`) – Interactive UI for:
  - Free text generation
  - Text summarization
  - Query classification

## 🚀 How to Run Locally

### Prerequisites
- Python 3.9+
- Google Cloud service account with **Gemini API** enabled (JSON key)
- Docker & Minikube (optional, for Kubernetes deployment)

### 1. Backend (FastAPI)
```bash
cd ml_app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account-key.json"
export LOGSTASH_HOST="localhost"
python -m uvicorn app:app --reload --port 8000
