from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from url_shortner.schemas.url_schema import URLCreate, URLResponse, URLListResponse, APIResponse
from url_shortner.services.url_service import URLService
from url_shortner.repositories.url_repository import URLRepository
from url_shortner.config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

logger = logging.getLogger(__name__) ###########

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_url_service(db: Session = Depends(get_db)) -> URLService:
    repo = URLRepository(db)
    return URLService(repo)

# Define router post/urls Morteza
# Fill
# Method
# Define router get/U Poorya
@router.get("/u/{short_code}", status_code=status.HTTP_302_FOUND)
# Method
def redirect_url(short_code: str, service: URLService = Depends(get_url_service)):
    try:
        original = service.get_original_url(short_code)
        return RedirectResponse(original)
    except HTTPException as e:
        return APIResponse(status="failure", message=e.detail), e.status_code
@router.post("/urls", status_code=status.HTTP_201_CREATED)
def create_url(url: URLCreate, service: URLService = Depends(get_url_service)):
    try:
        new_url = service.create_short_url(str(url.original_url))
        return APIResponse(status="success", data=URLResponse.from_orm(new_url).dict())
    except HTTPException as e:
        return APIResponse(status="failure", message=e.detail), e.status_code
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

# Define router get/urls Morteza
# Fill
# Method
@router.get("/urls")
def get_all_urls(service: URLService = Depends(get_url_service)):
    try:
        urls = service.get_all_urls()
        data = [URLResponse.from_orm(u).dict() for u in urls]
        return APIResponse(status="success", data=data)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

# Define router delete/urls Poorya
@router.delete("/urls/{short_code}")
# Method
def delete_url(short_code: str, service: URLService = Depends(get_url_service)):
    try:
        service.delete_url(short_code)
        return APIResponse(status="success", message="URL deleted successfully"), status.HTTP_204_NO_CONTENT
    except HTTPException as e:
        return APIResponse(status="failure", message=e.detail), e.status_code  # to get real 404 error code "raise e"