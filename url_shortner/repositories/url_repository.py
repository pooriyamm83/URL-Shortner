from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from url_shortner.models.url import URL

class URLRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self):
        return

    def get_by_short_code(self):
        return

    def get_all(self):
        return

    def delete(self):
        return

    # Bonus later
