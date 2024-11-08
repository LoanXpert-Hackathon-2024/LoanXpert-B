from sqlalchemy.orm import Session
from app.models.user import User

def get_investor_by_id(investor_id: int, db: Session):
    return db.query(User).filter(User.id == investor_id, User.role == "inversionista").first()

# Puedes añadir otras funciones específicas para inversionistas aquí
