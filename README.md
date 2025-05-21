# 🔍 RAG Chatbot

A lightweight Retrieval-Augmented Generation (RAG) chatbot built with Streamlit and LangChain, featuring semantic search capabilities without requiring an LLM.

## 📝 Introduction

This project implements a RAG-based chatbot that uses semantic search to find and present relevant information from a knowledge base. Unlike traditional RAG implementations, this version focuses on efficient retrieval without the overhead of an LLM, making it perfect for quick information lookup and demonstration purposes.

## ✨ Features

- **Semantic Search**: Find relevant information using natural language queries
- **Lightweight Architecture**: No LLM required, reducing costs and complexity
- **Streamlit Interface**: Clean, user-friendly web interface
- **FAISS Vector Store**: Efficient similarity search and retrieval
- **Sentence Transformers**: High-quality embeddings for semantic understanding

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit**: Web interface
- **LangChain**: Framework for RAG implementation
- **FAISS**: Vector similarity search
- **Sentence Transformers**: Text embeddings
- **Pandas**: Data manipulation
- **TikToken**: Token counting utilities

## 🏗️ Architecture Overview

The application follows a simple but effective architecture:

1. **Data Layer**
   - CSV-based knowledge base
   - Document conversion to LangChain format

2. **Vector Store**
   - FAISS for efficient similarity search
   - Sentence Transformers for embeddings

3. **Retrieval Layer**
   - Semantic search implementation
   - Top-k retrieval strategy

4. **Presentation Layer**
   - Streamlit web interface
   - Real-time query processing

## 🚀 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone [repository-url]
   cd RAG_Chatbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app/main.py
   ```

## 💻 Usage

1. Open your web browser and navigate to `http://localhost:8501`
2. Enter your question in the text input field
3. The chatbot will search the knowledge base and return relevant information
4. Results are displayed in a clean, formatted manner

## 📁 Folder Structure

```
RAG_Chatbot/
├── app/
│   ├── __init__.py
│   ├── main.py          # Streamlit application entry point
│   ├── chatbot.py       # Chatbot implementation
│   ├── retriever.py     # Vector store and retrieval logic
│   └── utils.py         # Utility functions
├── data/
│   └── knowledge_base.csv  # Knowledge base data
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 👥 Author

[Sreyangshu Sarkar]

## 📞 Contact

For questions and support, please open an issue in the GitHub repository.
