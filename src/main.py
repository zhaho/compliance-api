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

# @app.get("/api/hosts/{host_id}", status_code=status.HTTP_200_OK, tags=['Hosts'])
# async def get_host(host_id: int = Path(gt=0)):
#     for host in HOSTS:
#         if host.id == host_id:
#             return host

# @app.post("/api/hosts", status_code=status.HTTP_201_CREATED, tags=['Hosts'])
# async def create_host(host_request: HostRequest):
#     new_host = Host(**host_request.model_dump())
#     HOSTS.append(find_host_id(new_host))

# @app.put("/api/hosts/{host_id}", status_code=status.HTTP_201_CREATED, tags=['Hosts'])
# async def update_host(host: HostRequest):
#     host_changed = False
#     for i in range(len(HOSTS)):
#         if HOSTS[i].id == host.id:
#             HOSTS[i] = host
#             host_changed = True
    
#     if not host_changed:
#         raise HTTPException(status_code=404, detail="Item not found")

# @app.delete("/api/hosts/{host_id}", status_code=status.HTTP_201_CREATED, tags=['Hosts'])
# async def delete_host(host_id: int = Path(gt=0)):
#     host_changed = False
#     for i in range(len(HOSTS)):
#         if HOSTS[i].id == host_id:
#             HOSTS.pop(i)
#             host_changed = True
#             break
    
#     if not host_changed:
#         raise HTTPException(status_code=404, detail="Item not found")



# @app.get("/api/teams", status_code=status.HTTP_200_OK, tags=['Teams'])
# async def get_all_teams():
#     return TEAMS

# @app.get("/api/teams/{team_id}", status_code=status.HTTP_200_OK, tags=['Teams'])
# async def get_team(team_id: int = Path(gt=0)):
#     for team in TEAMS:
#         if team.id == team_id:
#             return team

# @app.post("/api/teams", status_code=status.HTTP_201_CREATED, tags=['Teams'])
# async def create_team(team_request: TeamRequest):
#     new_team = Team(**team_request.model_dump())
#     TEAMS.append(find_team_id(new_team))


# @app.put("/api/teams/{team_id}", status_code=status.HTTP_201_CREATED, tags=['Teams'])
# async def update_team(team: TeamRequest):
#     team_changed = False
#     for i in range(len(TEAMS)):
#         if TEAMS[i].id == team.id:
#             TEAMS[i] = team
#             team_changed = True
    
#     if not team_changed:
#         raise HTTPException(status_code=404, detail="Item not found")



# @app.delete("/api/teams/{team_id}", status_code=status.HTTP_201_CREATED, tags=['Teams'])
# async def delete_team(team_id: int = Path(gt=0)):
#     team_changed = False
#     for i in range(len(TEAMS)):
#         if TEAMS[i].id == team_id:
#             TEAMS.pop(i)
#             team_changed = True
#             break
    
#     if not team_changed:
#         raise HTTPException(status_code=404, detail="Item not found")


# def find_host_id(host: Host):
#     host.id = 1 if len(HOSTS) == 0 else HOSTS[-1].id + 1
#     return host

# def find_team_id(team: Team):
#     team.id = 1 if len(TEAMS) == 0 else TEAMS[-1].id + 1
#     return team