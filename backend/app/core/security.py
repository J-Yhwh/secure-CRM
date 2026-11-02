


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

def get_current_user(token: str = Depends(oauth2_scheme)):
  credentials_exception = HTTP_Execution(
    status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    # TODO: load the actual user from the database here
    return {"username": username, "role": payload.get("role", "Viewer")}

def role_required(allowed_roles: list):
    def role_checker(current_user: dict = Depends(get_current_user)):
        if current_user.get("role") not in allowed_roles:
            raise HTTPException(status_code=403, detail="Operation forbidden for your role")
        return current_user
    return role_checker

