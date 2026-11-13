import os
from dotenv import load_dotenv

load_dotenv()

def env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}

WEBHOOK_TOKEN = os.getenv("WEBHOOK_TOKEN", "")
DATABASE_PATH = os.getenv("DATABASE_PATH", "./data/ai_soc_sentinel.db")
RISK_EMAIL_THRESHOLD = int(os.getenv("RISK_EMAIL_THRESHOLD", "70"))
AI_ENABLED = env_bool("AI_ENABLED", False)
AI_API_KEY = os.getenv("AI_API_KEY", "")
AI_MODEL = os.getenv("AI_MODEL", "")
AI_BASE_URL = os.getenv("AI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
AI_TIMEOUT_SECONDS = int(os.getenv("AI_TIMEOUT_SECONDS", "15"))
SMTP_ENABLED = env_bool("SMTP_ENABLED", False)
SMTP_HOST = os.getenv("SMTP_HOST", "")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
SMTP_FROM = os.getenv("SMTP_FROM", "")
SOC_ANALYST_EMAIL = os.getenv("SOC_ANALYST_EMAIL", "")
SMTP_STARTTLS = env_bool("SMTP_STARTTLS", True)
