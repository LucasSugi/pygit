FROM python:3.7-slim-buster
RUN apt-get update \
    && apt-get install -y \
        git \
    && rm -rf /var/lib/apt/lists/*
RUN pip install pandas==1.3.5 openpyxl==3.0.9
WORKDIR /src
COPY extract_git_deletion.py .