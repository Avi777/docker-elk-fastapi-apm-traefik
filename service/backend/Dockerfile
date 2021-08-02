FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

LABEL maintainer="avishekh@fusemachines.com"

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app