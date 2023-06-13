FROM python:3.10-alpine as base

WORKDIR /code
 
COPY ./requirements.txt /code/requirements.txt
 
RUN python -m venv /code/env
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./api /code/api
COPY ./startserver.sh /code/startserver.sh

CMD ["/code/startserver.sh"]