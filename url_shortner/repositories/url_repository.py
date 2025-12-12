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
    def get_by_short_code(self):
        return

    # Morteza
    def get_all(self):
        return

    # Poorya
    def delete(self):
        return

    # Bonus later
