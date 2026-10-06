from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TextAnalysisRequest(BaseModel):
    user_id: int
    text: str


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/ping")
async def app_ping():
    return {"status": "ok", "message": "Zmistex API is running"}


@app.post("/analyze/text")
async def analyze_text(request: TextAnalysisRequest):
    return {
        "status": "success",
        "received_text": request.text,
        "user": request.user_id
    }