import sys
import os
# ✅ Prevent Streamlit + Torch crash on Windows
os.environ['STREAMLIT_SERVER_WATCH_DIRS'] = 'false'

# ✅ Add parent dir for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.utils import load_csv, dataframe_to_documents
from app.retriever import create_vector_store
from app.chatbot import SimpleChatBot

# Load data
df = load_csv("data/knowledge_base.csv")
docs = dataframe_to_documents(df)
vectorstore = create_vector_store(docs)
chatbot = SimpleChatBot(vectorstore)

st.title("🔍 RAG Chatbot")
query = st.text_input("Enter your question:")

if query:
    with st.spinner("Searching..."):
        answer = chatbot.ask(query)
    st.markdown(f"**Answer:**\n{answer}")
