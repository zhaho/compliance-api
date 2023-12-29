from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from src.models import Teams
from src.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class TeamRequest(BaseModel):
    name: str = Field(min_length=3)
    when_changed: str = Field(min_length=1)
    when_created: str = Field(min_length=1)

@router.get("/api/teams", status_code=status.HTTP_200_OK, tags=['Teams'])
async def get_all_teams(db: db_dependency):
    return db.query(Teams).all()
