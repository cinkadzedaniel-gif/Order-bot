from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///tz.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = "tz_table"

    id =Column(Integer, primary_key=True)
    username = Column(String)
    types = Column(String)
    func = Column(String)
    budget = Column(String)


    Base.metadata.create_all(engine)

