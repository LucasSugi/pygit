FROM python:3.10-slim-buster
RUN apt-get update \
    && apt-get install -y \
        git \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /src
COPY /src .
