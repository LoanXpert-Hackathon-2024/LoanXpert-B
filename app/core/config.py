from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:adminadmin@localhost/LoanXpert"

settings = Settings()
