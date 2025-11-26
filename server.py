from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware

# Configure
genai.configure(api_key="AIzaSyD42OtCpFptg7qrN0Zs2GNLa6h83_p55ts")
MODEL = "models/gemini-2.5-flash"

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    prompt: str

@app.post("/gemini")
async def run_gemini(req: Prompt):
    model = genai.GenerativeModel(MODEL)
    response = model.generate_content(req.prompt)
    return {"text": response.text}
