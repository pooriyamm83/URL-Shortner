import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from url_shortner.config import DATABASE_URL, APP_TTL_MINUTES
from url_shortner.repositories.url_repository import URLRepository
from url_shortner.services.url_service import URLService
from url_shortner.models.url import URL
from datetime import datetime, timedelta

if __name__ == "__main__":
    print(f"Starting cleanup job... TTL = {APP_TTL_MINUTES} minutes")

    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()

    repo = URLRepository(db)
    service = URLService(repo)

    try:
        deleted_count = service.delete_expired_urls()
        print(f"Cleanup finished! Deleted {deleted_count} expired URLs.")
    except Exception as e:
        print(f"Error during cleanup: {e}")
    finally:
        db.close()