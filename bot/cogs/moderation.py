import discord
from discord.ext import commands


# Source: https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/mod.py
class MemberID(commands.Converter):
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


class Moderation(commands.Cog):
    '''
    Moderation tools for astoria.
    '''
    def __init__(self, bot):
        self.bot = bot

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
    async def ban(self, ctx, member: discord.Member, *, reason: str = None):
        '''
        Bans a user from the server.
        Usage: !ban [username]

        TODO: Option to add a reason for a ban
        '''
        await member.ban()
        await ctx.send(
            f"{member.name} has been banned from the server."
        )

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: MemberID):
        '''
        Unbans a user from the server.
        Usage: !unban [user id number]
        '''
        await ctx.guild.unban(discord.Object(id=member))
        await ctx.send("User has been unbanned.")

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
        if not discord.utils.get(ctx.guild.roles, name=role_name):
            # Muted role does not exist, create it
            perm = discord.Permissions(    # defaults to no permissions allowed
                read_message_history=True
            )
            await ctx.guild.create_role(
                name=role_name,
                permissions=perm,
                reason="There was no 'Muted' role previously to mute members."
            )
            print("Created Muted role...")
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
        if not discord.utils.get(ctx.guild.roles, name=role_name):
            # Muted role does not exist, create it
            perm = discord.Permissions(    # defaults to no permissions allowed
                read_message_history=True
            )
            await ctx.guild.create_role(
                name=role_name,
                permissions=perm,
                reason="There was no 'Muted' role previously to mute members."
            )
            print("Created Muted role because it didn't exist before...")
        if not discord.utils.get(member.roles, name=role_name):
            # Member doesn't have Muted role6
            await ctx.send(f"{member.name} is already unmuted.")
        else:
            # Unmute user
            await member.remove_roles(role)
            await ctx.send(
                f"{member.name} has been unmuted."
            )


def setup(bot):
    bot.add_cog(Moderation(bot))
