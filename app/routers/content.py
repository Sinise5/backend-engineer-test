from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.deps import get_current_user
from app.schemas.content import ContentCreate, ContentOut, ContentUpdate
from app.crud import content as crud_content
from app.database import get_db
from app.models.user import User

router = APIRouter(prefix="/contents", tags=["Contents"])


@router.post("/", response_model=ContentOut)
def create_content(content: ContentCreate, db: Session = Depends(get_db), user : User = Depends(get_current_user)):
    content.owner_id = user.id
    return crud_content.create_content(db, content)


@router.get("/", response_model=list[ContentOut])
def read_contents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return crud_content.get_contents(db, skip=skip, limit=limit)


@router.get("/user/", response_model=list[ContentOut])
def read_contents_by_user(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return crud_content.get_contents_by_user(db, user.id, skip=skip, limit=limit)


@router.get("/{content_id}", response_model=ContentOut)
def read_content(content_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    db_content = crud_content.get_content(db, content_id)
    if not db_content:
        raise HTTPException(status_code=404, detail="Content not found")
    return db_content


@router.put("/{content_id}", response_model=ContentOut)
def update_content(content_id: int, content_update: ContentUpdate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    db_content = crud_content.get_content(db, content_id)
    if not db_content:
        raise HTTPException(status_code=404, detail="Content not found")
    return crud_content.update_content(db, db_content, content_update)


@router.delete("/{content_id}", response_model=ContentOut)
def delete_content(content_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    db_content = crud_content.get_content(db, content_id)
    if not db_content:
        raise HTTPException(status_code=404, detail="Content not found")
    return crud_content.delete_content(db, db_content)
