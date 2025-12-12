from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from url_shortner.models.url import URL
from datetime import datetime, timedelta
from url_shortner.config import APP_TTL_MINUTES

class URLRepository:
    def __init__(self, db: Session):
        self.db = db

    # Morteza
    def create(self, url: URL) -> URL:
        self.db.add(url)
        self.db.commit()
        self.db.refresh(url)
        return url

    # Poorya
    def get_by_short_code(self, short_code: str) -> URL | None:
        stmt = select(URL).where(URL.short_code == short_code)
        return self.db.scalar(stmt)

    # Morteza
    def get_all(self) -> list[URL]:
        stmt = select(URL)
        return self.db.scalars(stmt).all()

    # Poorya
    def delete(self, short_code: str) -> bool:
        stmt = delete(URL).where(URL.short_code == short_code)
        result = self.db.execute(stmt)
        self.db.commit()
        return result.rowcount > 0

    # Bonus later
    def delete_expired(self) -> int:
        expiration_time = datetime.utcnow() - timedelta(minutes=APP_TTL_MINUTES)
        stmt = delete(URL).where(URL.created_at < expiration_time)
        result = self.db.execute(stmt)
        self.db.commit()
        return result.rowcount