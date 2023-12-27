from fastapi import FastAPI

app = FastAPI(
    title="Compliance-API",
    summary="Compliance-API for seamless tracking and management of compliance hosts through a versatile set of endpoints, allowing CRUD operations and detailed filtering based on services, environments, owners, and teams.",
    version="0.0.1",
    contact={
        "name": "Kenneth Ros",
        "url": "http://github.com/zhaho",
    },
)


# filter by: main_service: str = "", environment: str = "", owner_email: str = "", team_id: int = 0
@app.get("/api/hosts", summary="Get all hosts", tags=['Hosts']) 
def index():
    return [{"hosts": "info"}]

@app.get("/api/hosts/{host_id}", summary="Get host by id", tags=['Hosts'])
def index():
    return [{"hosts": "info"}]

@app.post("/api/hosts", summary="Create host", tags=['Hosts'])
def index():
    return [{"hosts": "info"}]

@app.put("/api/hosts/{host_id}", summary="Update host", tags=['Hosts'])
def index():
    return [{"hosts": "info"}]

@app.delete("/api/hosts/{host_id}", summary="Delete host", tags=['Hosts'])
def index():
    return [{"hosts": "info"}]

@app.get("/api/teams", summary="Get all teams", tags=['Teams'])
def index():
    return [{"hosts": "info"}]

@app.get("/api/teams/{team_id}", summary="Get team by id", tags=['Teams'])
def index():
    return [{"hosts": "info"}]    

@app.post("/api/teams", summary="Create team", tags=['Teams'])
def index():
    return [{"hosts": "info"}]

@app.put("/api/teams/{team_id}", summary="Update team", tags=['Teams'])
def index():
    return [{"hosts": "info"}]

@app.delete("/api/teams/{team_id}", summary="Delete team", tags=['Teams'])
def index():
    return [{"hosts": "info"}]