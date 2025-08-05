from fastapi import APIRouter, Depends, Request
from slowapi import Limiter
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserRead, UserRegister, UserLogin, UserOut
from app.services.user_service import register_user, login_user
from slowapi.util import get_remote_address


router = APIRouter()

limiter = Limiter(key_func=get_remote_address)

@router.post("/token")
@limiter.limit("5/minute")  # ⛔ maksimal 5 kali per menit per IP
def login(request: Request, credentials: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, credentials)

@router.post("/register", response_model=UserRead)
def register(user: UserRegister, db: Session = Depends(get_db)):
    return register_user(db, user)

@router.post("/token")
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, credentials)
