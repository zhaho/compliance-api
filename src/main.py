from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException, Body
from pydantic import BaseModel, Field
from starlette import status
from src.database import engine
import src.models
from src.routers import hosts, teams, services

app = FastAPI(
    title="Compliance-API",
    summary="Compliance-API for seamless tracking and management of compliance hosts through a versatile set of endpoints, allowing CRUD operations and detailed filtering based on services, environments, owners, and teams.",
    version="1.0.0",
    contact={
        "name": "Kenneth Ros",
        "url": "http://github.com/zhaho",
    },
)

src.models.Base.metadata.create_all(bind=engine)

app.include_router(hosts.router)
app.include_router(teams.router)
app.include_router(services.router)