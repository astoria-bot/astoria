import os
import sqlalchemy as sqla
from dotenv import load_dotenv
from cogs.utils.database.models import Base

load_dotenv()

DB_USER = os.getenv('USERNAME')
DB_PASSWORD = os.getenv('PASSWORD')
DB_DATABASE = os.getenv('DATABASE')
DB_HOST = os.getenv('HOST')

class DBConfig:
    def __init__(self):
        e = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
        self.engine = sqla.create_engine(e)
        self.connection = self.engine.connect()
        self.metadata = sqla.MetaData()    # Used for representing a Table
        # Create the table
        Base.metadata.create_all(self.engine)

    def get_metadata(self):
        return self.metadata

    def get_engine(self):
        return self.engine

    def get_connection(self):
        return self.connection
