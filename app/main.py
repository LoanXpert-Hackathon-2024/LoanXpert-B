from fastapi import FastAPI
from app.api.v1.endpoints import auth, investor, borrower
from app.db.base import Base
from app.db.session import engine

app = FastAPI()

# Registrar los routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(investor.router, prefix="/investors", tags=["investors"])
app.include_router(borrower.router, prefix="/borrower", tags=["borrower"])
Base.metadata.create_all(bind=engine)