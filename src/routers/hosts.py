from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from src.models import Hosts
from src.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class HostRequest(BaseModel):
    name: str = Field(min_length=3)
    when_changed: str = Field(min_length=1)
    when_created: str = Field(min_length=1)

@router.get("/api/hosts", status_code=status.HTTP_200_OK, tags=['Hosts'])
async def get_all_hosts(db: db_dependency):
    return db.query(Hosts).all()
