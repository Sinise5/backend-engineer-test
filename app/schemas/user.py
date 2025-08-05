from datetime import datetime
import re
from pydantic import BaseModel, field_validator
from typing import Literal, Optional

class UserRegister(BaseModel):
    username: str
    full_name: Optional[str] = None
    password: str
    role: Optional[Literal["regular user", "admin"]] = "regular user"
    
    @field_validator("username")
    def username_must_be_alphanumeric(cls, v):
        if not re.match("^[a-zA-Z0-9_]+$", v):
            raise ValueError("Username hanya boleh huruf, angka, atau underscore")
        return v

    @field_validator("password")
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError("Password minimal 8 karakter")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password harus mengandung huruf kapital")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password harus mengandung huruf kecil")
        if not re.search(r"[0-9]", v):
            raise ValueError("Password harus mengandung angka")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError("Password harus mengandung simbol")
        return v


class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    full_name: Optional[str]
    role: str

    class Config:
        from_attributes = True

class UserRead(BaseModel):
    id: int
    username: str
    full_name: Optional[str]
    role: str
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    full_name: Optional[str]
    password: Optional[str]
    role: Optional[str]
    is_active: Optional[bool]
