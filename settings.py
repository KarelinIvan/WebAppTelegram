import os
from dotenv import load_dotenv

load_dotenv()

# Для работ с сервисом telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")