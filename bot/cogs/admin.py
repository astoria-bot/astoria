import discord
from discord.ext import commands


class Admin(commands.Cog):
    '''
    Administrative Tools for astoria.
    '''
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Admin(bot))
