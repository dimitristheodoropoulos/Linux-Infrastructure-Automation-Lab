import streamlit as st
import requests

st.set_page_config(page_title="Gemini AI Agentic Demo", layout="centered")
st.title("🤖 Agentic GenAI Assistant")
st.markdown("Powered by **Google Gemini API** – Agentic endpoints demonstration")

api_url = st.sidebar.text_input("Backend API URL", value="http://localhost:8000")
st.sidebar.markdown("---")
st.sidebar.markdown("### Agentic Capabilities")
st.sidebar.markdown("- 💬 Free text generation (`/llm-query`)")
st.sidebar.markdown("- 📄 Summarization agent (`/agent/summarize`)")
st.sidebar.markdown("- 🏷️ Classification agent (`/agent/classify`)")

tab1, tab2, tab3 = st.tabs(["💬 Generate", "📄 Summarize", "🏷️ Classify"])

with tab1:
    query = st.text_area("Ask anything:", height=100, placeholder="Explain quantum computing...")
    if st.button("Generate", key="gen"):
        if query:
            with st.spinner("Generating response..."):
                try:
                    r = requests.get(f"{api_url}/llm-query/{query}", timeout=60)
                    if r.status_code == 200:
                        st.success("Response:")
                        st.write(r.json().get("response", "No response"))
                    else:
                        st.error(f"Error {r.status_code}: {r.text[:300]}")
                except Exception as e:
                    st.error(f"Connection error: {e}")

with tab2:
    user_text = st.text_area("Paste text to summarize:", height=150)
    sentences = st.slider("Number of sentences in summary", 1, 5, 3)
    if st.button("Summarize", key="sum"):
        if user_text:
            with st.spinner("Agent summarizing..."):
                try:
                    r = requests.get(f"{api_url}/agent/summarize/{user_text[:2000]}", params={"sentences": sentences}, timeout=60)
                    if r.status_code == 200:
                        data = r.json()
                        st.success(f"Summary ({data.get('sentences', sentences)} sentences):")
                        st.write(data.get("summary", "No summary"))
                        st.caption(f"Original length: {data.get('original_length', 0)} chars")
                    else:
                        st.error(f"Error {r.status_code}: {r.text[:300]}")
                except Exception as e:
                    st.error(f"Connection error: {e}")

with tab3:
    classify_text = st.text_input("Enter a sentence to classify:", placeholder="How to install Python?")
    if st.button("Classify", key="cls"):
        if classify_text:
            with st.spinner("Agent classifying..."):
                try:
                    r = requests.post(f"{api_url}/agent/classify", json={"query": classify_text}, timeout=30)
                    if r.status_code == 200:
                        data = r.json()
                        st.success(f"Category: **{data.get('category', 'unknown')}**")
                    else:
                        st.error(f"Error {r.status_code}: {r.text[:300]}")
                except Exception as e:
                    st.error(f"Connection error: {e}")

st.markdown("---")
st.caption("Note: 429 errors mean Gemini API quota exceeded. Try later or use different model.")
