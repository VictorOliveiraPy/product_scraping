#!/bin/bash

# Executa o arquivo run_crawl.py
python3 run_crawl.py &

# Inicia o FastAPI usando o Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
