from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.schema import CreateTable


engine = create_engine('sqlite:///taskmanager.db', echo=True)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass

