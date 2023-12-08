import pytest
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Guild(Base):
    """Guild table for testing"""
    __tablename__ = "guild"
    id = Column("id", String(50), primary_key=True)
    guild_id = Column("guild_id", String(50))
    name = Column("name", String(50))

@pytest.fixture
def db_engine():
    """Database for testing"""
    engine = create_engine('mysql://username:password@localhost/test_database', echo=True)
    yield engine
    # Clean up the database after the tests
    engine.dispose()

@pytest.fixture
def session(db_engine):
    """Create a session for the test database"""
    Session = sessionmaker(bind=db_engine)
    return Session()
