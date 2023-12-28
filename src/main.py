from typing import Optional
from fastapi import FastAPI, Path, Query, HTTPException, Body
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI(
    title="Compliance-API",
    summary="Compliance-API for seamless tracking and management of compliance hosts through a versatile set of endpoints, allowing CRUD operations and detailed filtering based on services, environments, owners, and teams.",
    version="0.0.1",
    contact={
        "name": "Kenneth Ros",
        "url": "http://github.com/zhaho",
    },
)

class Host:
    id: int
    hostname: str
    main_service: str
    environment: str
    owner_email: str
    team_id: int

    def __init__(self, id, hostname, main_service, environment, owner_email, team_id):
        self.id = id
        self.hostname = hostname
        self.main_service = main_service
        self.environment = environment
        self.owner_email = owner_email
        self.team_id = team_id

class HostRequest(BaseModel):
    id: Optional[int] = None
    hostname: str = Field(min_length=3)
    main_service: str = Field(min_length=1)
    environment: str = Field(min_length=1)
    owner_email: str = Field(min_length=2)
    team_id: int = Field(gt=0)

    class Config:
        json_schema_extra = {
            'example': {
                'hostname': 'lxappkrlab01',
                'main_service': 'Service Name',
                'environment': 'PROD',
                'owner_email': "kenneth.ros@lindex.com",
                'team_id': 1
            }
        }

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

class TeamRequest(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=3)
    when_changed: str = Field(min_length=1)
    when_created: str = Field(min_length=1)

    class Config:
        json_schema_extra = {
            'example': {
                'name': 'Technical Services',
                'when_changed': '2023-12-31',
                'when_created': '2023-05-12',
            }
        }

HOSTS = [
    Host(1,'lxappkrlab01','Service Name 1','prod','kenneth.ros@lindex.com',1),
    Host(2,'lxappkrlab02','Service Name 2','qa','kenneth.ros@lindex.com',1),
    Host(3,'lxappkrlab03','Service Name 3','dev','zhaho.ros@gmail.com',2),
    Host(4,'lxappkrlab04','Service Name 4','temp','kenneth.ros@lindex.com',3),
    Host(5,'lxappkrlab05','Service Name 6','prod','kenneth.ros@lindex.com',3),
]

TEAMS = [
    Team(1,'Technical Services','2023-03-20','2023-03-20'),
    Team(2,'Service Desk','2023-04-31','2023-03-20'),
    Team(3,'Ecom','2023-03-31','2023-03-20'),
    Team(4,'Analytics','2023-05-31','2023-03-20'),
    Team(5,'Store Dev','2023-10-31','2023-03-20'),
    
]

@app.get("/api/hosts", status_code=status.HTTP_200_OK, tags=['Hosts'])
async def get_all_hosts():
    return HOSTS

@app.get("/api/hosts/{host_id}", status_code=status.HTTP_200_OK, tags=['Hosts'])
async def get_host(host_id: int = Path(gt=0)):
    for host in HOSTS:
        if host.id == host_id:
            return host

@app.post("/api/hosts", status_code=status.HTTP_201_CREATED, tags=['Hosts'])
async def create_host(host_request: HostRequest):
    new_host = Host(**host_request.model_dump())
    HOSTS.append(find_host_id(new_host))

@app.put("/api/hosts/{host_id}", status_code=status.HTTP_201_CREATED, tags=['Hosts'])
async def update_host(host: HostRequest):
    host_changed = False
    for i in range(len(HOSTS)):
        if HOSTS[i].id == host.id:
            HOSTS[i] = host
            host_changed = True
    
    if not host_changed:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/api/hosts/{host_id}", status_code=status.HTTP_201_CREATED, tags=['Hosts'])
async def delete_host(host_id: int = Path(gt=0)):
    host_changed = False
    for i in range(len(HOSTS)):
        if HOSTS[i].id == host_id:
            HOSTS.pop(i)
            host_changed = True
            break
    
    if not host_changed:
        raise HTTPException(status_code=404, detail="Item not found")



@app.get("/api/teams", status_code=status.HTTP_200_OK, tags=['Teams'])
async def get_all_teams():
    return TEAMS

@app.get("/api/teams/{team_id}", status_code=status.HTTP_200_OK, tags=['Teams'])
async def get_team(team_id: int = Path(gt=0)):
    for team in TEAMS:
        if team.id == team_id:
            return team

@app.post("/api/teams", status_code=status.HTTP_201_CREATED, tags=['Teams'])
async def create_team(team_request: TeamRequest):
    new_team = Team(**team_request.model_dump())
    TEAMS.append(find_team_id(new_team))


@app.put("/api/teams/{team_id}", status_code=status.HTTP_201_CREATED, tags=['Teams'])
async def update_team(team: TeamRequest):
    team_changed = False
    for i in range(len(TEAMS)):
        if TEAMS[i].id == team.id:
            TEAMS[i] = team
            team_changed = True
    
    if not team_changed:
        raise HTTPException(status_code=404, detail="Item not found")



@app.delete("/api/teams/{team_id}", status_code=status.HTTP_201_CREATED, tags=['Teams'])
async def delete_team(team_id: int = Path(gt=0)):
    team_changed = False
    for i in range(len(TEAMS)):
        if TEAMS[i].id == team_id:
            TEAMS.pop(i)
            team_changed = True
            break
    
    if not team_changed:
        raise HTTPException(status_code=404, detail="Item not found")


def find_host_id(host: Host):
    host.id = 1 if len(HOSTS) == 0 else HOSTS[-1].id + 1
    return host

def find_team_id(team: Team):
    team.id = 1 if len(TEAMS) == 0 else TEAMS[-1].id + 1
    return team