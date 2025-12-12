from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from url_shortner.models.url import URL

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
    def get_by_short_code(self):
        return

    # Morteza
    def get_all(self) -> list[URL]:
        stmt = select(URL)
        return self.db.scalars(stmt).all()

    # Poorya
    def delete(self):
        return

    # Bonus later
