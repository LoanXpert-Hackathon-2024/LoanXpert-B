# app/services/investor_service.py

import math
from typing import List, Dict
from sqlalchemy.orm import Session
from app.models.user import User

# Definir la comisión como una constante global
COMMISSION_RATE = 0.03  # 3% de comisión

def get_investor_by_id(investor_id: int, db: Session):
    return db.query(User).filter(User.id == investor_id, User.role == "inversionista").first()

def calculate_gain(capital: float, rate_of_return: float, min_months: int, max_months: int) -> List[Dict[str, float]]:
    results = []
    
    # Convertir la tasa anual de rentabilidad a decimal
    Ta = rate_of_return / 100

    # Calcular la tasa mensual Tm
    Tm = (1 + Ta) ** (1 / 12) - 1

    for M in range(min_months, max_months + 1):
        # Calcular el monto total acumulado Pt
        try:
            Pt = capital * (1 + Tm) ** M
        except ZeroDivisionError:
            # Manejo de casos de división por cero en la fórmula (si Tm es 0)
            Pt = 0

        # Calcular la ganancia total G después de aplicar la comisión
        G = Pt - ((Pt - capital) * COMMISSION_RATE) - capital  # Ganancia total para el periodo M

        # Redondear la ganancia total G a dos decimales
        G = round(G, 0)

        # Guardar el resultado para este número de meses
        results.append({
            "months": M,
            "total_gain": G  # Ganancia total al final del periodo M, redondeada
        })

    return results
