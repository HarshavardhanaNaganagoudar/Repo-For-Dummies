import os
from dotenv import load_dotenv
from pathlib import Path

# find project root
env_path = Path(__file__).resolve().parents[2] / ".env"

load_dotenv(env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")