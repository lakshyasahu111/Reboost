import os
from dotenv import load_dotenv

load_dotenv()

# Gemini config (via LiteLLM)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
LLM_MODEL = "gemini/gemini-2.5-flash"