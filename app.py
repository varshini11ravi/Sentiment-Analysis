import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import time
import json

# --- CONFIGURATION ---
# Ensure you have run: ollama pull llama3.2:1b
MODEL_ID = "llama3.2:1b"
OLLAMA_URL = "http://localhost:11434/api/generate"

st.set_page_config(page_title="2026 Local Sentiment", page_icon="🦙")

def query_ollama(text):
    """Sends a single request to the local Ollama instance"""
    prompt = f"""
    Analyze the sentiment of the following text. 
    Respond with ONLY one word: POSITIVE, NEGATIVE, or NEUTRAL.
    
    Text: {text}
    Sentiment:"""
    
    payload = {
        "model": MODEL_ID,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.1  # Low temperature for consistent classification
        }
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "NEUTRAL").strip().upper()
    except Exception as e:
        return f"ERROR: {str(e)}"

# --- STREAMLIT UI ---
st.title("🦙 2026 Local Sentiment (Ollama 1B)")
st.info(f"Running locally using {MODEL_ID}. Ensure Ollama is running (`ollama serve`).")

uploaded_file = st.file_uploader("Upload your sentiment_dataset.csv", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    if st.button("🚀 Analyze Locally"):
        if 'text' not in df.columns:
            st.error("CSV must contain a 'text' column.")
        else:
            with st.spinner("Processing locally via Ollama..."):
                start_time = time.time()
                predictions = []
                
                # Progress bar for local processing
                progress_bar = st.progress(0)
                for i, text in enumerate(df['text']):
                    label = query_ollama(text)
                    # Clean up any extra text the LLM might have added
                    clean_label = "NEUTRAL"
                    for possible in ["POSITIVE", "NEGATIVE", "NEUTRAL"]:
                        if possible in label:
                            clean_label = possible
                            break
                    predictions.append(clean_label)
                    progress_bar.progress((i + 1) / len(df))
                
                df['ai_prediction'] = predictions
                st.success(f"Processed {len(df)} rows in {time.time() - start_time:.2f}s")
                
                # Show Chart
                fig = px.bar(df['ai_prediction'].value_counts(), title="Sentiment Distribution")
                st.plotly_chart(fig)
                st.dataframe(df[['text', 'ai_prediction']])