#!/bin/bash
echo "▶️ Iniciando FastAPI via Uvicorn..."
poetry run uvicorn src.app.main:app --reload --port 8000
