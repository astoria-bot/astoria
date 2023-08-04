from discord import Status, Game
from discord.ext import commands


class Admin(commands.Cog):
    """Administrative tools for astoria."""

    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(name="setstatus")
    async def set_status(self, ctx, status: str = None):
        """Changes the status message of the bot."""
        if status is None:
            await ctx.send("No status was recevied. Status is unchanged.")
            return
        await self.bot.change_presence(status=Status.online, activity=Game(status))
        await ctx.send("Bot status has been changed!")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Admin(bot))
