from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Invite(Base):
    __tablename__ = "invites"

    invite_id = Column(String(255), primary_key=True)
    user_id = Column(String(255), ForeignKey("users.user_id"))
    user = relationship("User")
    count = Column(Integer, default=0)

class User(Base):
    __tablename__ = "users"

    user_id = Column(String(255), primary_key=True)
    count = Column(Integer, default=0)

engine = create_engine('sqlite:///invites.db')
Base.metadata.create_all(engine)
