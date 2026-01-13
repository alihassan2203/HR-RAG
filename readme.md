# Multimodal RAG for PDF Intelligence

Production-grade Retrieval-Augmented Generation (RAG) system for querying PDFs.

## Features
- PDF ingestion
- OpenAI embeddings
- Vector search (ChromaDB)
- LangChain orchestration
- Streamlit UI
- Unit tests
- Localhost deployment

## Run Locally
```bash
pip install -r requirements.txt
cp .env.example .env
streamlit run app/main.py
