import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = PROJECT_ROOT / ".env"

load_dotenv(dotenv_path=ENV_PATH, override=True)

AI_PROVIDER = os.getenv("AI_PROVIDER", "demo").lower()
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")