from sqlalchemy import create_engine
import os
import pytest


@pytest.fixture(scope="session")
def connection():
    engine = create_engine(
        "mysql+mysqldb://{}:{}@{}:{}/{}".format(
            os.environ.get("TEST_DB_USER"),
            os.environ.get("TEST_DB_PASSWORD"),
            os.environ.get("TEST_DB_HOST"),
            os.environ.get("TEST_DB_PORT"),
            os.environ.get("TEST_DB_NAME"),
        )
    )
    return engine.connect()


# class TestDatabase:
