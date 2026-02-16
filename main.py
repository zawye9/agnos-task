from fastapi import FastAPI
from datetime import datetime
from app.services import get_today_record
from app.config import SERVICE_NAME

app = FastAPI(title=SERVICE_NAME)

@app.get("/health")
def health():
    return {
        "status": "OK",
        "time": datetime.utcnow().isoformat()
    }

@app.get("/today")
def today():
    return get_today_record()
