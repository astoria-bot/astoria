from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self, ctx):
        """Displays a description about the bot.
        Usage: !about"""
        await ctx.send(
            """
            Hi I"m astoria! I"m a Discord bot made with Discord.py.
            \nFor a list of all my commands, type `!help`!
            \nYou can find my source code here:
            \nhttps://github.com/jgo28/astoria
            """
        )

    @commands.has_permissions(administrator=True)
    @commands.command(name="members")
    async def member_count(self, ctx, status: str = None):
        """Returns the number of members in the server.
        Usage: !members"""
        members = ctx.guild.member_count
        await ctx.send(members)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Info(bot))
