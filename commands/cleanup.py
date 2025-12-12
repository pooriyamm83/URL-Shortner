from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from url_shortner.config import DATABASE_URL, APP_TTL_MINUTES
from url_shortner.repositories.url_repository import URLRepository
from url_shortner.models.url import URL

if __name__ == "__main__":
    print(f"starting cleaning up expired URLs...")
    print(f"TTL active: {APP_TTL_MINUTES} minutes")

    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    repo = URLRepository(db)

    try:
        deleted_count = repo.delete_expired()
        print(f"Cleanup is successful")
        print(f"{deleted_count} expired URLs were deleted.")
    except Exception as e:
        print(f"Error in cleanup: {e}")
    finally:
        db.close()