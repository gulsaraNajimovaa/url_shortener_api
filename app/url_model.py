from sqlalchemy import Integer, String, Column

from app.database import Base


class UrlModel(Base):
    __tablename__ = "url"

    id = Column(Integer, primary_key=True)
    original_url = Column(String, index=True, unique=True)
    shortened_url = Column(String, index=True, unique=True)

