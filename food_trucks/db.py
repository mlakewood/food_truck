"""
    Module that contains all methods etc for creating and initialising the database
    and database connections for SQLAlchemy

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def get_engine(url):
    return create_engine(url, convert_unicode=True)

def get_db_session(engine):
    return scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
def init_db(engine, Base):
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from food_trucks.models.food_truck import FoodTruck
    Base.metadata.create_all(bind=engine)

Base = declarative_base()
