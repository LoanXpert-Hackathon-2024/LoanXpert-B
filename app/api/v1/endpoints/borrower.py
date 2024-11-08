from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.borrower_service import get_borrower_by_id
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{borrower_id}")
def read_borrower(borrower_id: int, db: Session = Depends(get_db)):
    borrower = get_borrower_by_id(borrower_id, db)
    if not borrower:
        raise HTTPException(status_code=404, detail="borrower not found")
    return borrower
