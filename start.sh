#!/bin/bash
set -e

poetry install

echo "Iniciando aplicação ..."
poetry run uvicorn src.app.main:app --host 0.0.0.0 --port 10000
