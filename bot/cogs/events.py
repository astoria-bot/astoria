import discord
from discord.ext import commands


class Events(commands.Cog):
    '''
    Event listeners for astoria.
    '''
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        '''
        Handles exception errors caused by commands.
        '''
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have the permissions required for this command.")
            return
        elif isinstance(error, commands.errors.CheckFailure):
            await ctx.send('You do not have the correct role for this command.')
            return
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send('I could not find that user. Please try again.')
            return
        raise error

def setup(bot):
    bot.add_cog(Events(bot))