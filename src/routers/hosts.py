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
    hostname: str = Field(min_length=3)
    main_service: str = Field(min_length=1)
    environment: str = Field(min_length=1)
    owner_email: str = Field(min_length=9)
    team_id: int = Field(gt=0)

@router.get("/api/hosts", status_code=status.HTTP_200_OK, tags=['Hosts'])
async def get_all_hosts(db: db_dependency):
    return db.query(Hosts).all()

@router.get("/api/hosts/{host_id}", status_code=status.HTTP_200_OK, tags=['Hosts'])
async def get_host(db: db_dependency, host_id: int = Path(gt=0)):
    host_model = db.query(Hosts).filter(Hosts.id == host_id).first()
    if host_model is not None:
        return host_model
    raise HTTPException(status_code=404, detail='Host not found.')

@router.post("/api/hosts", status_code=status.HTTP_201_CREATED, tags=['Hosts'])
async def create_host(db: db_dependency, host_request: HostRequest):
    # Convert all string fields to lowercase
    for field_name, field_value in host_request.dict().items():
        if isinstance(field_value, str):
            setattr(host_request, field_name, field_value.lower())

    # Add and commit to the database
    host_model = Hosts(**host_request.model_dump())
    db.add(host_model)
    db.commit()

@router.put("/api/hosts/{host_id}", status_code=status.HTTP_204_NO_CONTENT, tags=['Hosts'])
async def update_host(db: db_dependency, host_request: HostRequest,host_id: int = Path(gt=0)):
    # Convert all string fields to lowercase
    for field_name, field_value in host_request.dict().items():
        if isinstance(field_value, str):
            setattr(host_request, field_name, field_value.lower())

    # Add and commit to the database
    
    host_model = db.query(Hosts).filter(Hosts.id == host_id).first()
    if host_model is None:
        raise HTTPException(status_code=404, detail='Host not found.')

    host_model.hostname = host_request.hostname
    host_model.main_service = host_request.main_service
    host_model.environment = host_request.environment
    host_model.owner_email = host_request.owner_email
    host_model.team_id = host_request.team_id

    db.add(host_model)
    db.commit()

@router.delete("/api/hosts/{host_id}", status_code=status.HTTP_204_NO_CONTENT, tags=['Hosts'])
async def delete_host(db: db_dependency, host_id: int = Path(gt=0)):
    host_model = db.query(Hosts).filter(Hosts.id == host_id).first()
    if host_model is None:
        raise HTTPException(status_code=404, detail='Host not found.')
    db.query(Hosts).filter(Hosts.id == host_id).delete()
    db.commit()