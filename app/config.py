import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = "gpt-4o-mini"  # economical
MAX_ROUNDS = 4
TEMPERATURE = 0.8  # humour + variation
