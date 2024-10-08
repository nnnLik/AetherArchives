FROM python:3.12-slim AS base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random

RUN apt-get update \
    && apt-get install -y gcc libev4 libev-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/core

####################################################

FROM base AS dev_req

COPY pyproject.toml poetry.lock /app/core/

RUN python3 -m pip install poetry
COPY pyproject.toml poetry.lock /app/core/

RUN poetry export --with dev --without-hashes --format=requirements.txt > requirements.txt

####################################################

FROM base AS prod_req

COPY pyproject.toml poetry.lock /app/core/

RUN python3 -m pip install poetry
COPY pyproject.toml poetry.lock /app/core/

RUN poetry export --without dev --without-hashes --format=requirements.txt > requirements.txt

####################################################

FROM base AS dev

COPY --from=dev_req /app/core/requirements.txt /app/core/

RUN pip install -r requirements.txt

COPY ./ /app/core/
RUN chmod +x /app/core/entrypoint.sh

####################################################

FROM base AS prod

COPY --from=prod_req /app/core/requirements.txt /app/core/

RUN pip install -r requirements.txt

COPY ./ /app/core/
RUN chmod +x /app/core/entrypoint.sh
