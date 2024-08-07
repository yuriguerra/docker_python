from sqlalchemy import Column, String, Integer
from src.config import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    nome = Column(String)

    def __repr__(self) -> str:
        return f"Users [name={self.name}]"