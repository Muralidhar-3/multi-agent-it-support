import os
import google.generativeai as genai
from groq import Groq
from openai import OpenAI

# -------------------------
# Gemini (Planner / Reasoning)
# -------------------------
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def gemini_llm(prompt: str):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text


# -------------------------
# Groq (Fast Execution)
# -------------------------
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def groq_llm(prompt: str):
    response = groq_client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# -------------------------
# OpenRouter (Fallback)
# -------------------------
openrouter_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def openrouter_llm(prompt: str):
    response = openrouter_client.chat.completions.create(
        model="mistralai/mixtral-8x7b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content