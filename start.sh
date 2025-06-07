#!/bin/bash
set -e

poetry install

echo "Rodando migrações no banco de dados ..."
alembic upgrade head

echo "Iniciando aplicação ..."
poetry run uvicorn src.app.main:app --host 0.0.0.0 --port 10000
