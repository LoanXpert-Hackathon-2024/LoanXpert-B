# app/schemas/investor.py

from pydantic import BaseModel
from typing import List, Dict

class GainCalculatorInput(BaseModel):
    capital: float
    rate_of_return: float  # Tasa de rentabilidad como porcentaje
    min_months: int
    max_months: int

class GainCalculatorOutput(BaseModel):
    results: List[Dict[str, float]]  # Lista de resultados por cada mes en el rango
