"""Contains functions to manipulate User database tables."""
import logging
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import MultipleResultsFound

from bot.utils.database.models import dynamic_user_table


def add_user(engine, discord_id: str, username: str, guild_id):
    """Adds a new user to the database."""
    with Session(engine) as session:
        if user_exists(engine, discord_id, guild_id):
            logging.debug(
                "%s:%s wasn't added because their discord_id "
                "already exists in the database!", discord_id, username
            )
            return
        # If discord_id doesn"t exist, add the user
        User = dynamic_user_table(guild_id)
        new_user = User(
            discord_id=discord_id,
            name=username,
        )
        try:
            session.add(new_user)
        except:
            session.rollback()
            raise
        session.commit()
        logging.debug("%s:%s has been added to guild%s.", discord_id, username, guild_id)

def user_exists(engine, discord_id: str, guild_id):
    """Checks to see if a user exists based on their discord_id.
    Returns true if user exists. Returns false if user does not exist."""
    with Session(engine) as session:
        # Queries just the discord_ids, not the entire object
        User = dynamic_user_table(guild_id)
        try:
            query = (
                session.query(User.discord_id)
                .filter(User.discord_id == discord_id)
                .scalar()
                is not None
            )
        except MultipleResultsFound:
            logging.error("Duplicate discord id's were found! Please check the database.")
        else:
            return query
