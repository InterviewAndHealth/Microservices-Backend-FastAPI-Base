from sqlalchemy import Column, Integer, String, TIMESTAMP, text

from app.database import Base, engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(TIMESTAMP, server_default=text("now()"))


User.metadata.create_all(engine)
