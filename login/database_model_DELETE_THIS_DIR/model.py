import reflex as rx
from sqlalchemy import create_engine

def get_engine() -> create_engine:
    return create_engine('sqlite:///./connect.db')

def get_Session():
    """
    Función para obtener una sesión de la base de datos.
    """
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=get_engine())
    return Session()

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)


# An Example of a db model u can use

Base.metadata.create_all(bind=get_engine())
