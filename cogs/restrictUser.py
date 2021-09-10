import discord
from discord import client
from discord.client import Client
from discord.ext import commands
from discord import Emoji
from discord.utils import get

class restrictUser(commands.Cog):

    def __init__(self, black):
        self.client = black

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online in restrict user')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def restrictUser(self, ctx, user: discord.User, *, Channel:discord.TextChannel= None):
        guild = ctx.guild
        channels = await guild.fetch_channels()
        channel2 = discord.utils.get(channels, id=844527629057916928)
        overwrite1 = discord.PermissionOverwrite()
        overwrite1.view_channel=False
        embedChannel=discord.Embed(title='Person Restricted.', description=f'Restricted the following user: {user.name} ❌', color=0xcc0000)
        embedRestrict=discord.Embed(title=f'Person restricted. User:{user}', description='The following person was banned from the below mentioned channel', color=0xcc0000)
        embedRestrict.add_field(name=f'Moderator:{ctx.author.name}',value=f'Channel: {Channel.name}')
        await Channel.set_permissions(user, overwrite=overwrite1)
        await ctx.channel.send(embed=embedChannel)
        await channel2.send(embed=embedRestrict)


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unrestrict(self, ctx, user: discord.User, *, Channel:discord.TextChannel= None):
        guild = ctx.guild
        channels = await guild.fetch_channels()
        channel2 = discord.utils.get(channels, id=844527629057916928)
        overwrite2 = discord.PermissionOverwrite()
        overwrite2.view_channel=True
        embedUnrestrict=discord.Embed(title=f'Person unrestricted. User:{user}', description='The following person was unbanned from the below mentioned channel', color=0x8fcc00)
        embedUnrestrict.add_field(name=f'Moderator:{ctx.author.name}',value=f'Channel: {Channel.name}')
        embedChannel=discord.Embed(title='Person Unrestricted.', description=f'Unrestricted the following user: {user.name} ✅')
        await Channel.set_permissions(user, overwrite=overwrite2)
        await ctx.channel.send(embed=embedChannel)
        await channel2.send(embed=embedUnrestrict)


def setup(black):
    black.add_cog(restrictUser(black))
