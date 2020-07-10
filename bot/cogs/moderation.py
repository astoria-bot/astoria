import discord
from cogs.utils.metadata import MemberID
from discord.ext import commands

MemberID = MemberID()


class Moderation(commands.Cog):
    '''
    Moderation tools for astoria.
    '''
    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        '''
        Error handling for Moderation Cog commands.
        '''
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send("The role could not be found.")
            return
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("A user needs to be specified.")
            return

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        '''
        Kicks a user from the server.
        Usage: !kick [username]
        '''
        await member.kick()
        await ctx.send(
            f"{member.name} has been kicked from the server."
        )

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(
        self, ctx, member: discord.Member = None, *, reason: str = None
    ):
        '''
        Bans a user from the server.
        Usage: !ban [username]

        TODO: Option to add a reason for a ban
        '''
        if member is not None:
            await member.ban()
            await ctx.send(
                f"{member.name} has been banned from the server."
            )
        else:
            await ctx.send("A user needs to be specified.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: MemberID = None):
        '''
        Unbans a user from the server.
        Usage: !unban [user id number]
        '''
        if member is not None:
            await ctx.guild.unban(discord.Object(id=member))
            await ctx.send("User has been unbanned.")
        else:
            await ctx.send("A user ID needs to be specified.")

    @commands.has_permissions(manage_channels=True)
    @commands.command(name='nchannel')
    async def new_channel(self, ctx, channel_name='text channel'):
        '''
        Creates new text channel.
        Usage: !nchannel [username (optional)]
        '''
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f"Creating a new channel called {channel_name}.")
            await guild.create_text_channel(channel_name)

    @commands.has_permissions(manage_roles=True)
    @commands.command(name='role')
    async def role(self, ctx, member: discord.Member, role: discord.Role):
        '''
        If the user has the role, removes it. If the user does not have the
        role, assigns it to them.
        Usage: !role [username] [role name]
        '''
        if role in member.roles:    # User already has the role; remove it
            await member.remove_roles(role)
            await ctx.send(
                f"The {role.name} role was removed from {member.name}."
            )
        else:   # User does not have role, assign it to them
            await member.add_roles(role)
            await ctx.send(
                f"The {role.name} role has been assigned to {member.name}."
            )

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        '''
        Mutes a user from text channels.
        Usage: !mute [username]
        '''
        role_name = "Muted"
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        # Assign muted role to user
        await member.add_roles(role)
        await ctx.send(
            f"{member.name} has been muted."
        )

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        '''
        Unmutes a user from text channels.
        Usage: !unmute [username]
        '''
        role_name = "Muted"
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if not discord.utils.get(member.roles, name=role_name):
            # Member doesn't have Muted role6
            await ctx.send(f"{member.name} is already unmuted.")
        else:
            # Unmute user
            await member.remove_roles(role)
            await ctx.send(
                f"{member.name} has been unmuted."
            )

    @commands.has_permissions(manage_messages=True, read_message_history=True)
    @commands.command()
    async def clear(self, ctx, msgs: int = 1):
        '''
        Deletes the specified amount of messages. Delete 1 message by default
        Usage: !clear [number (optional)]
        '''
        if msgs > 100:
            await ctx.send("Limit of messages that can be deleted is 100.")
            return
        msgs = msgs + 1     # Delete the user's command message
        deleted = await ctx.channel.purge(limit=msgs)
        await ctx.send(f"Deleted {len(deleted)-1} message(s).", delete_after=3)

    @mute.error
    @unmute.error
    async def muted_error(self, ctx, error):
        '''
        Error handling specifically for the !mute and !unmute commands.
        '''
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send("Try running `!setup` to create a Muted role.")
            return


def setup(bot):
    bot.add_cog(Moderation(bot))
