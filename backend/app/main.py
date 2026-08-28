from fastapi import FastAPI
from app.api.routes import health

app = FastAPI()

#routes

app.include_router(health.router)

@app.get("/")
def read_root():
    return {"message": "Kyrgyz Readability Analyzer API is alive"}