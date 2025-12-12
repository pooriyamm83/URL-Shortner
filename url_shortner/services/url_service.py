from url_shortner.repositories.url_repository import URLRepository
from url_shortner.models.url import URL
from url_shortner.utils import encode_base62, validate_url
from fastapi import HTTPException

class URLService:
    def __init__(self, repo: URLRepository):
        self.repo = repo

    # Morteza
    def create_short_url(self):
        return

    # Poorya
    def get_original_url(self):
        return

    # Morteza
    def get_all_urls(self):
        return

    # Poorya
    def delete_url(self):
        return


    # Bonus later