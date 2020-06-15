FROM python:3.8.3-slim-buster

# Generate locale C.UTF-8 for postgres and general locale data
ENV LANG C.UTF-8

# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf
RUN set -x; \
        apt-get update \
        && apt-get install -y --no-install-recommends \
            ca-certificates \
            build-essential \
            libsasl2-dev \
            libldap2-dev \
            libssl-dev \
            curl \
            dirmngr \
            fonts-noto-cjk \
            gnupg \
            nodejs \
            npm \
            libxml2 \
            libxml2-dev \
            libxslt-dev \
            python3-dev \
            python3-renderpm \
            xz-utils \
            wkhtmltopdf \
            postgresql-client ;\
        apt-get remove -y --auto-remove ;\
        rm -rf /var/lib/apt/lists/*;

# Copy entrypoint script and Odoo configuration file

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

RUN adduser odoo
USER odoo
WORKDIR /usr/src/app