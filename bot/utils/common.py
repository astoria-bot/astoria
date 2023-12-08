"""Constants"""
from os import getenv
from dotenv import load_dotenv

# TODO: will need to be removed eventually
load_dotenv()

class DiscordConstants:
    """Constants for Discord"""
    TOKEN: str = getenv("DISCORD_TOKEN")
    GUILD_ID: str = getenv("DISCORD_GUILD")
    MAIN_CHANNEL: int = int(getenv("CHANNEL_ID"))

class BotConstants:
    """Constants specific to the bot design"""
    STATUS = "!help"  # Set bot status message here
    PREFIX = "!"  # Prefix to trigger bot commands on Discord

class DatabaseConstants:
    """Constants for the database"""
    ROOT_USERNAME: str = "root"
    ROOT_PASSWORD: str = getenv("MYSQL_ROOT_PASSWORD")
    USERNAME: str = getenv("MYSQL_USERNAME")
    PASSWORD: str = getenv("MYSQL_PASSWORD")
    HOST: str = getenv("MYSQL_HOST")
    DB_NAME: str = "astoria-db"
    DRIVERNAME: str = "mysqldb"
