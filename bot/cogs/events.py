import discord
from discord.ext import commands


class Events(commands.Cog):
    '''
    Event listeners for astoria.
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        '''
        Welcomes new members to the server.
        '''
        await member.create_dm()
        await member.dm_channel.send(
            f"Hi {member.name}, welcome to {member.guild.name}!"
        )
        channel = member.guild.system_channel
        await channel.send(f'{member.name} has joined the server!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        '''
        Handles exception errors caused by commands.
        '''
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(
                "You do not have the permissions required for this command."
            )
        elif isinstance(error, commands.errors.CheckFailure):
            await ctx.send(
                "You do not have the correct role for this command."
            )
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send(
                "I could not find what you specified. Please try again."
            )
        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send(
                "That command does not exist. See `!help` for my list of commands."
            )
        elif isinstance(error, commands.errors.CommandInvokeError):
            pass
        print(error)


def setup(bot):
    bot.add_cog(Events(bot))
