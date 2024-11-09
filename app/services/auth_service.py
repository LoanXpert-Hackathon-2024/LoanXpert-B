# app/services/auth_service.py

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import api_key_query, get_password_hash, verify_password, SECRET_KEY, ALGORITHM
from app.db.session import get_db

def register_user(user: UserCreate, db: Session):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        hashed_password=hashed_password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def get_current_user(db: Session = Depends(get_db), token: str = Depends(api_key_query)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
    return user