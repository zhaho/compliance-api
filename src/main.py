from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException, Body
from pydantic import BaseModel, Field
from starlette import status
from src.database import engine
import src.models
from src.routers import hosts, teams

app = FastAPI(
    title="Compliance-API",
    summary="Compliance-API for seamless tracking and management of compliance hosts through a versatile set of endpoints, allowing CRUD operations and detailed filtering based on services, environments, owners, and teams.",
    version="0.0.1",
    contact={
        "name": "Kenneth Ros",
        "url": "http://github.com/zhaho",
    },
)

class Team:
    id: int
    name: str
    when_changed: str
    when_created: str

    def __init__(self, id, name, when_changed, when_created):
        self.id = id
        self.name = name
        self.when_changed = when_changed
        self.when_created = when_created


src.models.Base.metadata.create_all(bind=engine)

app.include_router(hosts.router)
app.include_router(teams.router)