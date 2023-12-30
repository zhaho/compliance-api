from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from src.models import Hosts, Teams, Services
from src.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class ServiceRequest(BaseModel):
    servicename: str = Field(min_length=3)
    port: int = Field(gt=0)
    host_id: int = Field(gt=0)

@router.get("/api/v1/services", status_code=status.HTTP_200_OK, tags=['Services'])
async def get_all_services(db: db_dependency):
    services = db.query(Hosts, Services).join(Services, Hosts.id == Services.host_id).all()
    result = []
    for host, service in services:
        result.append({"host_id": host.id, "hostname": host.hostname, "servicename": service.servicename, "service_id": service.id, "port": service.port })
    if len(result) != 0:
        return result
    raise HTTPException(status_code=404, detail='Service not found.')

@router.get("/api/v1/services/{host_id}", status_code=status.HTTP_200_OK, tags=['Services'])
async def get_service(db: db_dependency, host_id: int = Path(gt=0)):
    services = db.query(Hosts, Services).join(Services, Hosts.id == Services.host_id).filter(Services.host_id == host_id).all()
    result = []
    for host, service in services:
        result.append({"host_id": host.id, "hostname": host.hostname, "servicename": service.servicename, "service_id": service.id, "port": service.port })
    if len(result) != 0:
        return result
    raise HTTPException(status_code=404, detail='Service not found.')

@router.get("/api/v1/services/find_by_servicename/", status_code=status.HTTP_200_OK, tags=['Services'])
async def get_service_by_name(db: db_dependency, service_name: str):
    services = db.query(Hosts, Services).join(Services, Hosts.id == Services.host_id).filter(Services.servicename == service_name.casefold()).all()
    result = []
    for host, service in services:
        result.append({"host_id": host.id, "hostname": host.hostname, "servicename": service.servicename, "service_id": service.id, "port": service.port })
    if len(result) != 0:
        return result
    raise HTTPException(status_code=404, detail='Service not found.')

@router.get("/api/v1/services/find_by_hostname/", status_code=status.HTTP_200_OK, tags=['Services'])
async def get_service_by_name(db: db_dependency, hostname: str):
    services = db.query(Hosts, Services).join(Services, Hosts.id == Services.host_id).filter(Hosts.hostname == hostname.casefold()).all()
    result = []
    for host, service in services:
        result.append({"host_id": host.id, "hostname": host.hostname, "servicename": service.servicename, "service_id": service.id, "port": service.port })
    if len(result) != 0:
        return result
    raise HTTPException(status_code=404, detail='Service not found.')

@router.post("/api/v1/services", status_code=status.HTTP_201_CREATED, tags=['Services'])
async def create_service(db: db_dependency, service_request: ServiceRequest):
    # Convert all string fields to lowercase
    for field_name, field_value in service_request.model_dump().items():
        if isinstance(field_value, str):
            setattr(service_request, field_name, field_value.lower())

    # Add and commit to the database
    service_model = Services(**service_request.model_dump())
    db.add(service_model)
    db.commit()

# @router.put("/api/v1/hosts/{host_id}", status_code=status.HTTP_204_NO_CONTENT, tags=['Hosts'])
# async def update_host(db: db_dependency, host_request: HostRequest,host_id: int = Path(gt=0)):
#     # Convert all string fields to lowercase
#     for field_name, field_value in host_request.dict().items():
#         if isinstance(field_value, str):
#             setattr(host_request, field_name, field_value.lower())

#     # Add and commit to the database
#     host_model = db.query(Hosts).filter(Hosts.id == host_id).first()
#     if host_model is None:
#         raise HTTPException(status_code=404, detail='Host not found.')

#     host_model.hostname = host_request.hostname
#     host_model.main_service = host_request.main_service
#     host_model.environment = host_request.environment
#     host_model.owner_email = host_request.owner_email
#     host_model.service_type = host_request.service_type
#     host_model.image_type = host_request.image_type
#     host_model.team_id = host_request.team_id

#     db.add(host_model)
#     db.commit()

# @router.delete("/api/v1/hosts/{host_id}", status_code=status.HTTP_204_NO_CONTENT, tags=['Hosts'])
# async def delete_host(db: db_dependency, host_id: int = Path(gt=0)):
#     host_model = db.query(Hosts).filter(Hosts.id == host_id).first()
#     if host_model is None:
#         raise HTTPException(status_code=404, detail='Host not found.')
#     db.query(Hosts).filter(Hosts.id == host_id).delete()
#     db.commit()