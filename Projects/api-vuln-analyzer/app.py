import streamlit as st
import requests

st.title("API Vulnerability Analyzer - AI Link Test")

# Using the host gateway address to reach the host's Ollama instance
ollama_url = "http://host.docker.internal:11434/api/tags"

try:
    response = requests.get(ollama_url)
    if response.status_code == 200:
        st.success("Successfully connected to DeepSeek on the Mint Host!")
        st.json(response.json())
    else:
        st.error(f"Connected, but got error: {response.status_code}")
except Exception as e:
    st.error(f"Failed to connect to host Ollama: {e}")


