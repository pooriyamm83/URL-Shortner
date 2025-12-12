from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from url_shortner.models.url import URL

class URLRepository:
    def __init__(self, db: Session):
        self.db = db

    # Morteza
    def create(self):
        return

    # Poorya
    def get_by_short_code(self, short_code: str) -> URL | None:
        stmt = select(URL).where(URL.short_code == short_code)
        return self.db.scalar(stmt)

    # Morteza
    def get_all(self):
        return

    # Poorya
    def delete(self, short_code: str) -> bool:
        stmt = delete(URL).where(URL.short_code == short_code)
        result = self.db.execute(stmt)
        self.db.commit()
        return result.rowcount > 0

    # Bonus later
