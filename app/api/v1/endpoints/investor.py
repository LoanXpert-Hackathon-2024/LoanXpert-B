from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.investor import GainCalculatorInput, GainCalculatorOutput
from app.services.investor_service import get_investor_by_id, calculate_gain
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


@router.post("/calculate-gain", response_model=GainCalculatorOutput)
def calculate_gain_endpoint(data: GainCalculatorInput):
    if data.capital <= 0 or data.min_months <= 0 or data.max_months < data.min_months or data.rate_of_return <= 0:
        raise HTTPException(status_code=400, detail="Todos los valores deben ser válidos y mayores que cero.")
    
    result = calculate_gain(data.capital, data.rate_of_return, data.min_months, data.max_months)
    return GainCalculatorOutput(results=result)