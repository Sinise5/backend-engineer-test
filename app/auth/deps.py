import os
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.core.config import settings


load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

SECRET_KEY = settings.SECRET_KEY

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = int(payload.get("sub"))
        token_username = payload.get("username")
        role = payload.get("role")
        if user_id is None or token_username is None or role is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter_by(id=user_id).first()
    if user is None:
        raise credentials_exception

    # Inject info dari token ke user object
    user.username_from_token = token_username
    user.role_from_token = role
    return user

