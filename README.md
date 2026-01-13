# HR-RAG

# Employee Handbook – RAG System

## Overview
This project is a **Retrieval-Augmented Generation (RAG)** system for querying an **Employee Handbook PDF** using natural language.  
It runs locally on **localhost** and provides accurate, source-based answers from official company policies.

## Covered Handbook Sections
- Employment basics and contract types  
- Equal opportunity and recruitment  
- Attendance and workplace policies  
- Confidentiality and data protection  
- Workplace harassment and violence  
- Workplace safety and emergency management  
- Drug-free and smoking policies  
- Employee Code of Conduct and dress code  
- Cybersecurity, internet, email, and social media usage  
- Conflict of interest and employee relationships  

## Architecture
PDF → Text Extraction → Embeddings → Vector DB → Retriever → LLM → UI


## Tech Stack
- Python 3.10+
- OpenAI GPT-4.1
- OpenAI Embeddings
- LangChain
- ChromaDB
- Streamlit
- PyMuPDF
- Pytest

## Key Features
- Natural-language policy search
- Source-grounded responses
- Modular, class-based Python code
- Persistent vector storage
- Localhost execution
- Unit tests

## Run Locally
```bash
pip install -r requirements.txt
cp .env.example .env
streamlit run app/main.py --server.address localhost --server.port 8501
## Testing
pytest
