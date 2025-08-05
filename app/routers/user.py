from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.deps import get_current_user
from app.database import get_db
from app.schemas.user import UserRegister, UserRead, UserUpdate
from app.crud import user as crud_user
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead)
def create(user_in: UserRegister, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if crud_user.get_user_by_username(db, user_in.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud_user.create_user(db, user.id)

@router.get("/", response_model=List[UserRead])
def read_users(db: Session = Depends(get_db), user = Depends(get_current_user)):
    users = crud_user.get_all_users(db)
    return users

@router.get("/{user_id}", response_model=UserRead)
def read(user_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    user = crud_user.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserRead)
def update(user_id: int, user_in: UserUpdate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    user = crud_user.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud_user.update_user(db, user, user_in)

@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    user = crud_user.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    crud_user.delete_user(db, user)
    return {"detail": "User deleted"}