from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/ping")
async def app_ping():
    return {"status": "ok", "message": "Zmistex API is running"}