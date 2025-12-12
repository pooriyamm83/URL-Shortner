from dotenv import load_dotenv
import os
import pathlib

load_dotenv(pathlib.Path(__file__).parent.parent / '.env')
DATABASE_URL = os.getenv("DATABASE_URL")
APP_TTL_MINUTES = int(os.getenv("APP_TTL_MINUTES", 1440))