import discord
from discord.ext import commands


class MemberID(commands.Converter):
    '''
    Source: https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/mod.py
    Used for getting the User ID for unbanning users.
    '''
    async def convert(self, ctx, argument):
        try:
            m = await commands.MemberConverter().convert(ctx, argument)
        except commands.BadArgument:
            try:
                return int(argument, base=10)
            except ValueError:
                raise commands.BadArgument(
                    f"{argument} is not a valid member or member ID."
                ) from None
        else:
            return m.id