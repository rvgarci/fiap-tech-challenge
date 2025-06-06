#!/bin/bash
echo "⏹️ Parando FastAPI via Uvicorn ..."
pkill -f "uvicorn src.app.main:app"
