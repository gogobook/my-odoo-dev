FROM python:3.8.1-slim-buster

# Generate locale C.UTF-8 for postgres and general locale data
ENV LANG C.UTF-8
RUN apt-get update \
        && apt-get install -y --no-install-recommends \
        ca-certificates \
        gcc \
        libc6-dev \
        curl \
        wget 


ENV RUSTUP_HOME=/usr/local/rustup \
    CARGO_HOME=/usr/local/cargo \
    PATH=/usr/local/cargo/bin:$PATH \
    RUST_VERSION=1.41.0

RUN set -eux; \
    url="https://static.rust-lang.org/rustup/archive/1.21.1/x86_64-unknown-linux-gnu/rustup-init"; \
    wget "$url"; \
    echo "ad1f8b5199b3b9e231472ed7aa08d2e5d1d539198a15c5b1e53c746aad81d27b *rustup-init" | sha256sum -c -; \
    chmod +x rustup-init; \
    ./rustup-init -y --no-modify-path --profile minimal --default-toolchain $RUST_VERSION; \
    rm rustup-init; \
    chmod -R a+w $RUSTUP_HOME $CARGO_HOME; \
    rustup --version; \
    cargo --version; \
    rustc --version;
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