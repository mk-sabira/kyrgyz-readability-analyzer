from fastapi import FastAPI
from app.api.routes import health, analyze

app = FastAPI()

#routes

app.include_router(health.router)
app.include_router(analyze.router)

@app.get("/")
def read_root():
    return {"message": "Kyrgyz Readability Analyzer API is alive"}