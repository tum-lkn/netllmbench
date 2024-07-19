FROM python:3.11.9

LABEL maintainer="kaan.aykurt@tum.de"
LABEL version="1.0"
LABEL description="Basic python environment for NETLLMBENCH"

RUN pip install --upgrade pip setuptools wheel

RUN pip install pyyaml==6.0.1 requests==2.31.0 ollama==0.2.0 langchain==0.2.1 langchain-community==0.2.1  \
    langchain-core==0.2.1 langchain-text-splitters==0.2.0 langchain-experimental==0.0.59

RUN pip install git+https://github.com/saghul/pyuv@master#egg=pyuv

RUN pip install "kathara"
