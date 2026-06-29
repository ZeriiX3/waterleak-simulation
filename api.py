# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Stockage en mémoire
results = []

class Result(BaseModel):
    t: float
    anomaly_ratio: float
    leak_detected: bool

@app.post("/results")
def push_result(r: Result):
    results.append({**r.dict(), "timestamp": datetime.now().isoformat()})
    return {"ok": True}

@app.get("/results")
def get_results():
    return results

@app.get("/results/latest")
def get_latest():
    if not results:
        return {"message": "Pas encore de résultats"}
    return results[-1]

@app.get("/status")
def get_status():
    if not results:
        return {"running": False, "leak_detected": False}
    return {
        "running": True,
        "leak_detected": results[-1]["leak_detected"],
        "last_update": results[-1]["timestamp"]
    }