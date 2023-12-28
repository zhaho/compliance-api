from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Hosts(Base):
    __tablename__ = 'hosts'

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String)
    main_service = Column(String)
    environment = Column(Integer)
    owner_email = Column(Integer)
    team_id = Column(Integer)
    