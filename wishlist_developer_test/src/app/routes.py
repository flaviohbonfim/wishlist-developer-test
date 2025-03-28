from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .schemas import UserCreate, UserResponse
from .crud import create_user, get_users

router = APIRouter()

# Dependência do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/users/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/api/users/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return get_users(db)
