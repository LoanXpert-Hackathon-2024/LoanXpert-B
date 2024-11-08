from sqlalchemy.orm import Session
from app.models.user import User

def get_borrower_by_id(borrower_id: int, db: Session):
    return db.query(User).filter(User.id == borrower_id, User.role == "prestamista").first()

# Puedes añadir otras funciones específicas para prestamistas aquí
