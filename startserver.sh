#!/bin/sh
source /code/env/bin/activate
gunicorn src.main:app --workers 4 --bind 0.0.0.0:80 --worker-class uvicorn.workers.UvicornWorker 