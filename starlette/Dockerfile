FROM python:3.8.5-slim-buster

# Generate locale C.UTF-8 for postgres and general locale data
ENV LANG C.UTF-8
RUN apt-get update \
        && apt-get install -y --no-install-recommends \
        ca-certificates \
        gcc \
        libc6-dev \
        curl \
        wget 


# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf
# RUN set -x; \
#         apt-get update \
#         && apt-get install -y --no-install-recommends \
#             ca-certificates \
#             build-essential \
#             libsasl2-dev \
#             libldap2-dev \
#             libssl-dev \
#             curl \
#             dirmngr \
#             fonts-noto-cjk \
#             gnupg \
#             nodejs \
#             node-less \
#             npm \
#             libxml2 \
#             libxml2-dev \
#             libxslt-dev \
#             python3-dev \
#             python3-renderpm \
#             xz-utils \
#             wkhtmltopdf \
#             postgresql-client 

# Copy entrypoint script and Odoo configuration file

COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

WORKDIR /usr/src/app