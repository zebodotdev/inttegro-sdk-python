# syntax=docker/dockerfile:1.7

FROM python:3.12-slim@sha256:78387bc3881b8273120a12ebe6c1ab22b018ccc2c9adf565ae1ac9b536e184ea AS base
WORKDIR /app
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY pyproject.toml poetry.lock requirements-bootstrap.txt README.md ./
COPY src ./src
COPY tests ./tests
RUN python -m pip install --no-cache-dir --require-hashes -r requirements-bootstrap.txt
RUN poetry config virtualenvs.create false
RUN poetry sync --with dev --no-interaction --no-ansi

# Build distribution artifacts (wheel + sdist)
FROM base AS dist
RUN poetry build --output /out

# CI target (use in GitHub Actions)
FROM base AS ci
RUN python -m unittest discover -s tests -p "test_*.py"

# Local/development target
FROM base AS dev
CMD ["bash"]
