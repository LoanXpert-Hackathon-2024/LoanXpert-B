# app/models/user.py

from sqlalchemy import Column, Integer, String
from app.db.base_class import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    hashed_password = Column(String)
    role = Column(String)  # Puede ser 'inversionista' o 'prestamista'
