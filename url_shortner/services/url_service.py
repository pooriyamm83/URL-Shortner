from url_shortner.repositories.url_repository import URLRepository
from url_shortner.models.url import URL
from url_shortner.utils import encode_base62, validate_url
from fastapi import HTTPException

class URLService:
    def __init__(self, repo: URLRepository):
        self.repo = repo

    # Morteza
    def create_short_url(self, original_url: str) -> URL:
        if not validate_url(original_url):
            raise HTTPException(status_code=400, detail="Invalid URL")
        url = URL(original_url=original_url, short_code="temp")  # Temp, update after ID
        url = self.repo.create(url)

        short_code = encode_base62(url.id)
        url.short_code = short_code
        self.repo.db.commit()
        self.repo.db.refresh(url)
        return url  # Update with short_code

    # Poorya
    def get_original_url(self, short_code: str) -> str:
        url = self.repo.get_by_short_code(short_code)
        if not url:
            raise HTTPException(status_code=404, detail="URL not found")
        return url.original_url

    # Morteza
    def get_all_urls(self) -> list[URL]:
        return self.repo.get_all()

    # Poorya
    def delete_url(self, short_code: str):
        if not self.repo.delete(short_code):
            raise HTTPException(status_code=404, detail="URL not found")


    # Bonus later