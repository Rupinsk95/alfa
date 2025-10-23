# Minimal FastAPI App

Minimalna aplikacja FastAPI z trzema endpointami:

- `/` - zwraca wiadomość z zmiennej środowiskowej `APP_MESSAGE`
- `/healthz` - endpoint zdrowia, zwraca `{"status": "ok"}`
- `/echo` (POST) - zwraca przesłaną wiadomość w formacie JSON

## Uruchomienie

1. Zainstaluj zależności:
```bash
pip install -r requirements.txt