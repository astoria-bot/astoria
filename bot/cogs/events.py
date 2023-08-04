"""Actions that occur during a particular event on Discord."""
from discord.ext import commands
from sqlalchemy.schema import CreateTable

from bot.utils.database.config import DatabaseConfiguration
from bot.utils.database.methods.user import add_user, user_exists
from bot.utils.database.methods.guild import guild_exists
from bot.utils.database.models import dynamic_user_table


class Events(commands.Cog):
    """Event listeners for astoria."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Events that occur when a new member joins a server the bot is
        apart of."""
        await member.create_dm()
        await member.dm_channel.send(
            f"Hi {member.name}, welcome to {member.guild.name}!"
        )
        channel = member.guild.system_channel
        await channel.send(f"{member.name} has joined the server!")
        # Add new user to database
        with DatabaseConfiguration() as engine:
            if not user_exists(engine, member.id, member.guild.id):
                add_user(engine, member.id, member.name, member.guild.id)
            

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """Events that occur when the bot joins a new guild."""
        with DatabaseConfiguration() as engine:
            if not guild_exists(engine, guild.id):
                table = dynamic_user_table(guild.id)
                CreateTable(table)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Handles exception errors caused by commands."""
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the permissions required for this command.")
        elif isinstance(error, commands.errors.CheckFailure):
            await ctx.send("You do not have the correct role for this command.")
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send("I could not find what you specified. Please try again.")
        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send(
                "That command does not exist. " "See `!help` for my list of commands."
            )
        elif isinstance(error, commands.errors.CommandInvokeError):
            pass
        print(error)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Events(bot))
