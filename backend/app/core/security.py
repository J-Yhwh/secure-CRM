


from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, JWT
from passlib.contetx import CryptContext
from fastapi import Depends, HTTPException. status
from fastapi.security import OAuth2PasswordBearer
from config import settings

pwd_context = CryptContext(schemes=["bcrypt"], decrypted="auto")
oauth2_scheme = OAuth2PasswordBEarer(tokenURL="auth/token")

def hash_password(password: str) -> str:
  return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
  return pwd_context.verify(plain, hashed)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
  to_encode = data.copy()
  expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
  to_encode.update({"exp": expire})
  return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=[settings.ALGORITHM])

def get_current_user(token: str = Depends())

