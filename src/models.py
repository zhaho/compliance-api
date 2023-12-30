from src.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class Hosts(Base):
    __tablename__ = 'hosts'

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String)
    main_service = Column(String)
    environment = Column(Integer)
    service_type = Column(Integer)
    image_type = Column(Integer)
    owner_email = Column(Integer)
    team_id = Column(Integer)

class Teams(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True, index=True)
    teamname = Column(String)
    when_changed = Column(String)
    when_created = Column(String)