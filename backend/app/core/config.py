

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  DATABASE_URL: str = "mysql+pymysql://crmuser:crmpass@db:3306/secure_crm"
  SECRET_KEY: str = "change-me-in-production"
  ALGORITHM: str = "HS256"
  ACCESS_TOKEN_EXPIRE_MINUTES: int = 15

  class Config:
    env_file = ".env"

settings = Settings()


  
