from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from db import models
from db.database import get_db
from db.crud import get_user_by_email,get_users,create_user as create_user1
from admin import schemas


router = APIRouter(prefix="/users")

@router.post("/user/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user1(db=db, user=user)


@router.get("/user/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users