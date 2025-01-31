from fastapi import FastAPI
from app.routes import generate

app = FastAPI()

app.include_router(generate.router, prefix="/api", tags=["pdf"])

@app.get("/")
async def root():
    return {"message": "Welcome to the PDF Text Extraction API"}
