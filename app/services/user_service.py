from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime, timezone

from app.auth.hash import hash_password, verify_password
from app.auth.jwt import create_access_token
from app.models.user import User
from app.schemas.user import UserRegister, UserLogin

def register_user(db: Session, user_data: UserRegister):
    if db.query(User).filter_by(username=user_data.username).first():
        raise HTTPException(status_code=400, detail="Username already registered")
    
    new_user = User(
        username=user_data.username,
        full_name=user_data.full_name,
        hashed_password=hash_password(user_data.password),
        role=user_data.role or "regular user"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login_user(db: Session, credentials: UserLogin):
    user = db.query(User).filter_by(username=credentials.username).first()
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    user.last_login_at = datetime.now(timezone.utc)
    db.commit()

    token = create_access_token({"sub": str(user.id), "username": user.username, "role": user.role})
    return {"access_token": token, "token_type": "bearer"}
