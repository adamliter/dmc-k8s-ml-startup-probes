# -*- mode: dockerfile; coding: utf-8; fill-column: 80; -*-
FROM python:3.13-slim-bullseye AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --compile-bytecode --no-editable --no-install-project
ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-editable --compile-bytecode

FROM python:3.13-slim
COPY --from=builder --chown=app:app /app/.venv /app/.venv
EXPOSE 8080
CMD ["/app/.venv/bin/start_server", "--host", "0.0.0.0", "--port", "8080"]
