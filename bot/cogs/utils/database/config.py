import os
import sqlalchemy as sqla
from dotenv import load_dotenv
from cogs.utils.database.models import Base

load_dotenv()

USER = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
DATABASE = os.getenv('DATABASE')
HOST = os.getenv('HOST')


class DBConfig:
    def __init__(self):
        e = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
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
