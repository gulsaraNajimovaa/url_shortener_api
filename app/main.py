import hashlib
import re
import time
from urllib.parse import urlparse

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from app.database import Base, engine, SessionLocal
from app.url_model import UrlModel

app = FastAPI()

Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
async def health():
    return {"message": "Hello from Url Shortener App"}


# noinspection PyTypeChecker
@app.post("/{create-short-url}")
async def create_short_url(
        original_url: str,
        db: Session = Depends(get_db)
):
    # check if we already have shortened_url in database
    db_original_url = db.query(UrlModel).filter(UrlModel.original_url == original_url).first()
    if db_original_url:
        return db_original_url

    # check if the url is valid
    if not re.search(r'^https://optom.app/', original_url):
        raise HTTPException(status_code=400, detail="Your provided URL is not valid")

    # if there isn't, create one
    current_time_ms = str(int(time.time() * 1000))  # Get current time in milliseconds as a string
    salted_url = original_url + current_time_ms  # Combine secret key with current time
    hashed = hashlib.sha256(salted_url.encode()).hexdigest()
    shortened_url = hashed[:5]

    db_url = UrlModel(original_url=original_url, shortened_url=shortened_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return "https://optom.app/" + shortened_url


# noinspection PyTypeChecker
@app.get("/{shortened_domain_url}")
async def get_original_url(
        shortened_domain_url: str,
        db: Session = Depends(get_db)
):
    parsed_url = urlparse(shortened_domain_url)
    shortened_url = parsed_url.path.strip('/')

    db_shortened_url = db.query(UrlModel).filter(UrlModel.shortened_url == shortened_url).first()

    return RedirectResponse(db_shortened_url.original_url, status_code=301)
