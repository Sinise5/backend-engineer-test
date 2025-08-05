from sqlalchemy.orm import Session
from app.models.content import Content
from app.schemas.content import ContentCreate, ContentUpdate


def get_content(db: Session, content_id: int):
    return db.query(Content).filter(Content.id == content_id).first()


def get_contents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Content).offset(skip).limit(limit).all()


def get_contents_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Content).filter(Content.owner_id == user_id).offset(skip).limit(limit).all()


def create_content(db: Session, content: ContentCreate):
    db_content = Content(**content.dict())
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content


def update_content(db: Session, db_content: Content, updates: ContentUpdate):
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(db_content, key, value)
    db.commit()
    db.refresh(db_content)
    return db_content


def delete_content(db: Session, db_content: Content):
    db.delete(db_content)
    db.commit()
    return db_content
