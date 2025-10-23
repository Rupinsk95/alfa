FROM python:3.12-slim AS builder

WORKDIR /app

RUN groupadd -g 1001 appgroup && useradd -m -u 1001 -g appgroup appuser

COPY requirements.txt .

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && pip install --no-cache-dir --prefix=/install -r requirements.txt \
    && apt-get purge -y build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN chown -R appuser:appgroup /app


FROM gcr.io/distroless/python3

WORKDIR /app

COPY --from=builder /app /app
COPY --from=builder /install /usr/local

EXPOSE 8000

USER 1001:1001


CMD ["/usr/local/bin/python3", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

