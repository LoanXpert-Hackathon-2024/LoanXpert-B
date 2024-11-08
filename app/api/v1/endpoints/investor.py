from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.investor_service import get_investor_by_id
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{investor_id}")
def read_investor(investor_id: int, db: Session = Depends(get_db)):
    investor = get_investor_by_id(investor_id, db)
    if not investor:
        raise HTTPException(status_code=404, detail="Investor not found")
    return investor
