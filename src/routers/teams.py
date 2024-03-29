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
    teamname: str = Field(min_length=3)
    when_changed: str = Field(min_length=1)
    when_created: str = Field(min_length=1)

@router.get("/api/v1/teams", status_code=status.HTTP_200_OK, tags=['Teams'])
async def get_all_teams(db: db_dependency):
    return db.query(Teams).all()


@router.get("/api/v1/teams/{team_id}", status_code=status.HTTP_200_OK, tags=['Teams'])
async def get_team(db: db_dependency, team_id: int = Path(gt=0)):
    team_model = db.query(Teams).filter(Teams.id == team_id).first()
    if team_model is not None:
        return team_model
    raise HTTPException(status_code=404, detail='Team not found.')

@router.post("/api/v1/teams", status_code=status.HTTP_201_CREATED, tags=['Teams'])
async def create_team(db: db_dependency, team_request: TeamRequest):
    # Convert all string fields to lowercase
    for field_name, field_value in team_request.dict().items():
        if isinstance(field_value, str):
            setattr(team_request, field_name, field_value.lower())

    # Add and commit to the database
    team_model = Teams(**team_request.model_dump())
    db.add(team_model)
    db.commit()

@router.put("/api/v1/teams/{team_id}", status_code=status.HTTP_204_NO_CONTENT, tags=['Teams'])
async def update_team(db: db_dependency, team_request: TeamRequest, team_id: int = Path(gt=0)):
    # Convert all string fields to lowercase
    for field_name, field_value in team_request.dict().items():
        if isinstance(field_value, str):
            setattr(team_request, field_name, field_value.lower())

    team_model = db.query(Teams).filter(Teams.id == team_id).first()
    if team_model is None:
        raise HTTPException(status_code=404, detail='Team not found.')

    team_model.teamname = team_request.teamname
    team_model.when_changed = team_request.when_changed
    team_model.when_created = team_request.when_created

    db.add(team_model)
    db.commit()

@router.delete("/api/v1/teams/{team_id}", status_code=status.HTTP_204_NO_CONTENT, tags=['Teams'])
async def delete_team(db: db_dependency, team_id: int = Path(gt=0)):
    team_model = db.query(Teams).filter(Teams.id == team_id).first()
    if team_model is None:
        raise HTTPException(status_code=404, detail='Team not found.')
    db.query(Teams).filter(Teams.id == team_id).delete()
    db.commit()
