import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL")

if not API_KEY or not MODEL:
    raise RuntimeError("GEMINI_API_KEY and GEMINI_MODEL must be set in .env")

client = genai.Client(api_key=API_KEY)

app = FastAPI(
    title="AI Question Answer API",
    description="A FastAPI application that uses Google Gemini to answer user questions.",
    version="1.0.0"
)


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "AI Question Answer API is running"
    }


@app.post("/generate")
def generate_answer(data: Question):

    if not data.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=data.question
        )

        if not response.text:
            raise HTTPException(
                status_code=500,
                detail="No response received from Gemini"
            )

        return {
            "question": data.question,
            "answer": response.text
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"AI service unavailable: {str(e)}"
        )