import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-4o-mini"

if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY not set in environment")
