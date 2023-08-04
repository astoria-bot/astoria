"""Handles database creation and connection."""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import URL
from sqlalchemy.schema import CreateTable
from dotenv import load_dotenv

from bot.utils.database.models import Guild

load_dotenv()
USERNAME = getenv("DB_USERNAME")
PASSWORD = getenv("DB_PASSWORD")
HOST = getenv("DB_HOST")


class DatabaseConfiguration:
    """Database configuration + context manager"""

    def __init__(self):
        self.engine = None
        self.connection = None
        self.metadata = None

    def __enter__(self):
        """Create database connection."""
        url = URL.create(
            drivername="mysqldb",
            username=USERNAME,
            password=PASSWORD,
            host=HOST,
            database="astoria-db",
        )
        self.engine = create_engine(url)
        self.connection = self.engine.connect()
        self.initialize_guild_table()
        self.metadata = MetaData()
        print("Connected to database.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Cleanup database connection when done."""
        if exc_tb is None:
            self.connection.commit()
        else:
            self.connection.rollback()
        self.connection.close()

    def get_metadata(self):
        """Returns tables associated with the database."""
        return self.metadata

    def get_engine(self):
        """Returns engine used to interact with database."""
        return self.engine

    def initialize_guild_table(self):
        """Initializes the guild database table. There should only be one at
        all times."""
        if not self.engine.dialect.has_table(self.engine, "guild"):
            CreateTable(Guild)
            print("Table has been created.")
        else:
            print("Table already exists.")
