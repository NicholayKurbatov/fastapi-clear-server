#!/bin/sh
source /code/env/bin/activate
gunicorn src.main:app --workers 4 --bind 0.0.0.0:80 --worker-class uvicorn.workers.UvicornWorker --access-logfile dbms_template_path/gunicorn/access.log --error-logfile dbms_template_path/gunicorn/error.log