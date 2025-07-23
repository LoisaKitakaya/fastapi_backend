import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")


@app.get("/")
def read_root():
    return {"Hello": "World"}
