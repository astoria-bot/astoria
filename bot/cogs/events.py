import discord
from discord.ext import commands


class Events(commands.Cog):
    '''
    Events for astoria.
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        '''
        Checks when errors occur during bot commands.
        '''
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the permissions required for this command.")
            return
        raise error

def setup(bot):
    bot.add_cog(Events(bot))