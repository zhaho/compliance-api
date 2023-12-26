from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return [{"hello": "world!"}]

@app.post("/api/hosts", summary="Create host")
def index():
    return [{"hosts": "info"}]

@app.get("/api/hosts", summary="Get all hosts")
def index():
    return [{"hosts": "info"}]

@app.get("/api/hosts/{host_id}", summary="Get host")
def index():
    return [{"hosts": "info"}]

@app.delete("/api/hosts/{host_id}", summary="Delete host")
def index():
    return [{"hosts": "info"}]

@app.put("/api/hosts", summary="Update host")
def index():
    return [{"hosts": "info"}]