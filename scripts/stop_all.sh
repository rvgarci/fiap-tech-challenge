#!/bin/bash
echo "⏹️ Parando FastAPI (Uvicorn) e Streamlit ..."

pkill -f "uvicorn src.app.main:app"
pkill -f "streamlit run streamlit_app/app.py"
