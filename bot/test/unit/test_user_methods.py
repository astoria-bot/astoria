import logging
from unittest.mock import patch
import pytest
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from bot.utils.database.methods.user import add_user, user_exists

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    discord_id: Mapped[str] = mapped_column(String(50))
    name: Mapped[str] = mapped_column(String(50))


def test_add_user_does_not_exist(db_engine):
    with patch("bot.utils.database.methods.user.user_exists", return_value=False):
        add_user(db_engine, discord_id='123', username='testuser', guild_id='456')

        # Query the database to check if the user was added
        Session = sessionmaker(bind=db_engine)
        with Session() as session:
            queried_user = session.query(User).filter_by(discord_id='123').first()

        assert queried_user is not None
        assert queried_user.name == 'testuser'


def test_add_user_exists(db_engine):
    with patch("bot.utils.database.methods.user.user_exists", return_value=True):
        add_user(db_engine, discord_id='123', username='testuser', guild_id='456')

        # Ensure that the user was not added
        Session = sessionmaker(bind=db_engine)
        with Session() as session:
            queried_user = session.query(User).filter_by(discord_id='123').first()

        assert queried_user is None
        # assert logging.debug.called_with(
        #     "123:testuser wasn't added because their discord_id already exists in the database!"
        # )
