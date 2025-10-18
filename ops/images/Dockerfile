FROM python:3.12-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

COPY . .

FROM gcr.io/distroless/python3

WORKDIR /app

COPY --from=builder /app /app
COPY --from=builder /install /usr/local

EXPOSE 8000

CMD ["/usr/local/bin/python3", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

