import streamlit as st
from dotenv import load_dotenv
from rag import create_vector_store

# Load environment variables
load_dotenv()

# Streamlit Page Config
st.set_page_config(page_title="AI Return Agent", page_icon="📦", layout="centered")

# Custom Styling for Highlights
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #4F46E5;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #6B7280;
        text-align: center;
        margin-bottom: 2rem;
    }
    .result-card {
        background-color: #1E293B;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 6px solid #6366F1;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<div class="main-title">📦 AI Return Policy Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Instant answers powered by RAG technology</div>', unsafe_allow_html=True)

# Cache the vector store loading
@st.cache_resource
def get_vector_store():
    return create_vector_store()

with st.spinner("Initializing knowledge base..."):
    vector_store = get_vector_store()

# Sample Suggestion Buttons
st.write("**Quick Questions:**")
col1, col2, col3 = st.columns(3)

if col1.button("🕒 Return Window"):
    st.session_state["user_query"] = "What is the return policy window?"
if col2.button("🧾 Missing Receipt"):
    st.session_state["user_query"] = "Can I return an item without a receipt?"
if col3.button("📦 Opened Items"):
    st.session_state["user_query"] = "Are opened or used products eligible for a full refund?"

# Text Input
default_val = st.session_state.get("user_query", "")
query = st.text_input("Ask any question about store returns:", value=default_val, placeholder="e.g., How long do refunds take?")

# Output Section
if query:
    with st.spinner("Searching policies..."):
        results = vector_store.similarity_search(query, k=1)
        
        if results:
            st.markdown("### 💡 Found Policy Answer:")
            st.info(results[0].page_content)
        else:
            st.warning("No relevant information found in policy document.")