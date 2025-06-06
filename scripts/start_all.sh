#!/bin/bash
set -e
echo "▶️ Iniciando FastAPI + Streamlit ..."

# Inicia o Uvicorn em segundo plano
poetry run uvicorn src.app.main:app --reload --port 8000 &

# Armazena o PID do Uvicorn
UVICORN_PID=$!

# Inicia o Streamlit (em foreground)
poetry run streamlit run streamlit_app/app.py

# Ao encerrar o Streamlit, finaliza o Uvicorn também
kill $UVICORN_PID
