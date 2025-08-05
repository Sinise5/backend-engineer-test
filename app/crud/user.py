from sqlalchemy.orm import Session
from app.auth.hash import hash_password
from app.models.user import User
from app.schemas.user import UserRegister, UserUpdate


def create_user(db: Session, user_in: UserRegister) -> User:
    user = User(
        username=user_in.username,
        full_name=user_in.full_name,
        hashed_password=hash_password(user_in.password),
        role=user_in.role or "regular user"  # default jika None atau kosong
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user



def get_user(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_username(db: Session, username: str) -> User:
    return db.query(User).filter(User.username == username).first()


def update_user(db: Session, db_user: User, user_in: UserUpdate) -> User:
    if user_in.full_name is not None:
        db_user.full_name = user_in.full_name
    if user_in.password is not None:
        db_user.hashed_password = hash_password(user_in.password)
    if user_in.role is not None:
        db_user.role = user_in.role
    if user_in.is_active is not None:
        db_user.is_active = user_in.is_active
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, db_user: User):
    db.delete(db_user)
    db.commit()