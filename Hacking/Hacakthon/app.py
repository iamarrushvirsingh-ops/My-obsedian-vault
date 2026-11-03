import os
import time
import pypdf
import streamlit as st
from dotenv import load_dotenv
from google import genai
from concurrent.futures import ThreadPoolExecutor

# Load environment variables from local .env file
load_dotenv()

# --- PAGE CONFIGURATION & DARK GLASSMORPHISM THEME ---
st.set_page_config(
    page_title="PreClass - Fast-Track Class Prep", 
    page_icon="🎓", 
    layout="centered"
)

st.markdown("""
<style>
    /* Dark Theme Background */
    .stApp { 
        background-color: #0E1117; 
        color: #FFFFFF; 
    }
    
    /* Modern Glassmorphism Headers for Outputs */
    .stMarkdown div[data-testid="stMarkdownContainer"] > h3 { 
        color: #00E5FF; 
        border-bottom: 2px solid #1F2937; 
        padding-bottom: 8px; 
    }
    
    /* Metric / Stat Card Container */
    div[data-testid="metric-container"] { 
        background: rgba(255, 255, 255, 0.05); 
        border: 1px solid rgba(255, 255, 255, 0.1); 
        border-radius: 10px; 
        padding: 15px; 
    }
    
    /* Action Button Styling with Hover Effect */
    .stButton>button { 
        background: linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%); 
        color: white; 
        border: none; 
        border-radius: 8px; 
        font-weight: bold; 
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        box-shadow: 0px 0px 15px rgba(124, 58, 237, 0.6);
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)


# --- 1. PDF TEXT EXTRACTION FUNCTION ---
def extract_text_from_pdf(pdf_file):
    """Opens an uploaded PDF file and extracts plain text page by page."""
    reader = pypdf.PdfReader(pdf_file)
    extracted_text = ""
    for index, page in enumerate(reader.pages):
        page_text = page.extract_text()
        if page_text:
            extracted_text += f"\n--- Page {index + 1} ---\n" + page_text
    return extracted_text


# --- 2. MULTI-AGENT WORKERS ---

def run_prerequisite_agent(client, context):
    """Agent 1: Specialized in identifying background prerequisite gaps."""
    prompt = (
        "You are an expert academic advisor. Analyze these course notes and list "
        "3-5 core prerequisite concepts or background knowledge a student MUST "
        "know before reading this lecture:\n\n"
        f"{context}"
    )
    response = client.models.generate_content(
        model="gemini-3.8-flash", 
        contents=prompt
    )
    return f"### 1. Prerequisites to Know\n{response.text}"


def run_brief_agent(client, context):
    """Agent 2: Specialized in generating a high-yield summary."""
    prompt = (
        "You are a concise academic tutor. Provide a high-yield summary "
        "of the main topic covered in these lecture notes in under 120 words:\n\n"
        f"{context}"
    )
    response = client.models.generate_content(
        model="gemini-3.8-flash", 
        contents=prompt
    )
    return f"### 2. 2-Minute Class Brief\n{response.text}"


def run_trajectory_agent(client, context):
    """Agent 3: Specialized in forecasting upcoming concepts."""
    prompt = (
        "Predict 2-3 logical next sub-topics or concepts that will likely "
        "be covered in the upcoming lecture based on these notes:\n\n"
        f"{context}"
    )
    response = client.models.generate_content(
        model="gemini-3.8-flash", 
        contents=prompt
    )
    return f"### 3. Upcoming Topic Preview\n{response.text}"


def run_multi_agent_pipeline(notes_text):
    """
    Orchestrates 3 parallel Gemini worker agents using ThreadPoolExecutor.
    """
    # Grab key from .env locally or Streamlit Secrets in cloud deployment
    api_key = os.environ.get("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", None)
    
    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing! Set it in your .env file or Streamlit secrets.")

    client = genai.Client(api_key=api_key)
    
    # Context truncation to prevent latency spikes
    context = notes_text[:6000]

    # Execute agents concurrently
    with ThreadPoolExecutor(max_workers=3) as executor:
        f1 = executor.submit(run_prerequisite_agent, client, context)
        f2 = executor.submit(run_brief_agent, client, context)
        f3 = executor.submit(run_trajectory_agent, client, context)

        res_prereq = f1.result()
        res_brief = f2.result()
        res_traj = f3.result()

    return f"{res_prereq}\n\n{res_brief}\n\n{res_traj}"


# --- 3. STREAMLIT WEB DASHBOARD ---
st.title("🎓 PreClass")
st.subheader("Upload your lecture notes & get ready for class in seconds.")
st.markdown("---")

uploaded_file = st.file_uploader("Drop your class notes PDF here", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF uploaded successfully!")
    
    if st.button("Generate PreClass Brief 🚀", type="primary"):
        start_time = time.time()
        
        with st.spinner("Dispatching Multi-Agent Gemini Orchestrator..."):
            try:
                extracted_text = extract_text_from_pdf(uploaded_file)
                
                if not extracted_text.strip():
                    st.error("Could not extract text from PDF. Ensure it's not an image-only scan.")
                else:
                    prep_brief = run_multi_agent_pipeline(extracted_text)
                    exec_time = round(time.time() - start_time, 2)
                    
                    st.markdown("---")
                    
                    # Display Live Latency & Performance Metrics
                    c1, c2, c3 = st.columns(3)
                    c1.metric(label="⚡ Prep Time Saved", value="95%", delta="Under 2 Mins")
                    c2.metric(label="⏱️ AI Latency", value=f"{exec_time}s", delta="Parallel Execution")
                    c3.metric(label="🤖 Multi-Agent Core", value="3 Agents", delta="Gemini 3.8 Flash")

                    st.markdown("---")
                    st.subheader("📌 Your PreClass Summary")
                    st.markdown(prep_brief)
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")