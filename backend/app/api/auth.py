# Copyright (c) 2026. Jac LL
# ALL Rights Reserved.
# All unauthorized use or distribution is prohibited.

from fastapi import FastAPI, DEPENDS, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta


#CONFIGURATION
SECRET_KEY = "your-secret-key"
ALGORITHM = HS256
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFESH_TOKEN_EMPIRE_DAYS = 7

pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()


## -- Security Utilities --
def hash_password(password: str):
  return pwd_context.hash(password)

def verify_Password(plain, hashed):
  return pwd_context.verify(plain, hashed)

def create_token(data: dict, expires_delta: timedelta):
  to_encode = data.copy()
  expire = datetime.utcnow() + expires delta
  return jwt.code(to_encode, SECRET KEY, algorithm=ALGORITHM)

# ----Role Dependency ---
def role_required(allowed_roles: list):
  def role_checker(current_user: dict = Depends(get_current_user)):
    if current_user["role"] not in allowed_roles:
      raise HTTPException(status_code=403, detail="Operation forbidden for your role. Please ensure ")
    return current_user
  return role_checker
  
