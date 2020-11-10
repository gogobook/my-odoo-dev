FROM python:3.8.6-slim-buster

# Generate locale C.UTF-8 for postgres and general locale data
ENV LANG C.UTF-8
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        gcc \
        libc6-dev \
        curl \
        wget \
        ;\
    apt-get remove -y --auto-remove \
        wget \
        ; \
    rm -rf /var/lib/apt/lists/*;


COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

WORKDIR /usr/src/app