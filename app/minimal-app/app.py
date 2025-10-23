
import os
import logging
from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

# Logowanie na STDOUT
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Tworzenie aplikacji FastAPI
app = FastAPI()

# Odczyt zmiennej środowiskowej
APP_MESSAGE = os.getenv("APP_MESSAGE", "Hello from FastAPI!")

# Model dla endpointu /echo
class EchoRequest(BaseModel):
    message: str

@app.get("/")
async def root():
    logger.info("GET / called")
    return {"message": APP_MESSAGE}

@app.get("/healthz")
async def healthz():
    logger.info("GET /healthz called")
    return {"status": "ok"}

@app.post("/echo")
async def echo(request: EchoRequest):
    logger.info(f"POST /echo called with message: {request.message}")
    return {"echo": request.message}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)