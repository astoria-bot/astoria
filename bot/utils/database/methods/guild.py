"""Contains functions to manipulate Guild database tables."""
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import MultipleResultsFound
import sqlalchemy as sqla

from bot.utils.database.models import Guild


def add_guild(engine, guild_id: str, guild_name: str):
    """Adds guild to database."""
    with Session(engine) as session:
        if guild_exists(engine, guild_id):
            print(
                f"{guild_id}:{guild_id} wasn't added because their guild_id "
                "already exists in tname database!"
            )
            return
        # If guild_id doesn't exist, add the guild
        new_guild = Guild(
            guild_id=guild_id,
            name=guild_name,
        )
        session.add(new_guild)
        session.commit()
        print(f"{id}:{guild_name} has been added to the database.")


def guild_exists(engine, guild_id: str):
    """Verify if a specified guild exists in database."""
    with Session(engine) as session:
        # Queries just the discord_ids, not the entire object
        try:
            query = (
                session.query(Guild.guild_id)
                .filter(Guild.guild_id == guild_id)
                .scalar()
                is not None
            )
        except MultipleResultsFound:
            print("Duplicate guild_id's were found! " "Please check the database.")
        else:
            return query


def update_guild(engine, guild_id: str, guild_name: str):
    """Update guild name with a given guild id."""
    pass


def delete_guild(engine, guild_id: str):
    """Removes guild from database."""
    pass


def delete_all(engine):
    """Deletes all guilds from database."""
    pass


def get_guild(engine, guild_id: str):
    """Returns data about a guild from database."""
    with Session(engine) as session:
        if guild_exists(engine, id):
            guild = session.query(Guild).filter(Guild.guild_id == guild_id).scalar()
            return {"name": guild.name, "guild_id": guild.guild_id}
        print("User was not found.")


def get_guild_count(engine):
    """Returns number of guilds in the database."""
    with Session(engine) as session:
        return session.query(Guild).count()
