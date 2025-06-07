#!/bin/bash
poetry install
poetry run uvicorn src.app.main:app --host 0.0.0.0 --port 10000
