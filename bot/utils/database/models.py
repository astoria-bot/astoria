"""Contains definitions for tables for the database. Each server will have a
table containing all users in that server. There will only be one Guild table
at all times."""
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column


class Guild(DeclarativeBase):
    """Uses guild ids to identify Discord servers the bot is in"""

    __tablename__ = "guild"
    id: Mapped[int] = mapped_column(primary_key=True)
    guild_id: Mapped[str] = mapped_column(String(50))
    name: Mapped[str] = mapped_column(String(50))

    def __repr__(self):
        return (
            f"Guild(id={self.id!r}, name={self.name!r}, " "guild_id={self.guild_id!r})"
        )

def dynamic_user_table(guild_id):
    """Dynamically build a model class based on the User model. Intention
    is to be able to create a table per Discord server containing all users."""

    class User(DeclarativeBase):
        """Table containing all the users in a given Discord server"""

        __tablename__ = f"guild_{guild_id}"
        id: Mapped[int] = mapped_column(primary_key=True)
        discord_id: Mapped[str] = mapped_column(String(50))
        name: Mapped[str] = mapped_column(String(50))

        def __repr__(self):
            return (
                f"User(id={self.id!r}, discord_id={self.discord_id!r}, "
                "name={self.name!r})"
            )

    return User
