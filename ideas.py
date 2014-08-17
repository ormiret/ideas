from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from project_name import project_name

Base = declarative_base()

class Idea(Base):
    __tablename__ = 'idea'
    name = Column(String(20), primary_key=True)
    description = Column(String(1000))
    creator = Column(String(50))

class Dependency(Base):
    __tablename__ = 'dependency'
    id = Column(Integer, primary_key=True)
    idea_name = Column(String(20), ForeignKey('idea.name'))
    depends =  Column(String(20), ForeignKey('idea.name'))

DB = "sqlite:////home/ormiret/webapps/ideas/htdocs/ideas/ideas.db"

def setup_db():
    engine = create_engine(DB)
    Base.metadata.create_all(engine)

def get_session():
    engine = create_engine(DB)
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    return DBSession()

def insert_idea(desc, creator):
    session = get_session()
    name = project_name()
    while not len(session.query(Idea).filter(Idea.name == name).all()) == 0:
        name = project_name()
    idea = Idea(name=name, description=desc, creator=creator)
    session.add(idea)
    session.commit()
    return name
