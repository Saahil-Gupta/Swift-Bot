import discord
from discord import client
from discord.client import Client
from discord.ext import commands
from discord.utils import get


class banChannel(commands.Cog):

    def __init__(self, ferrari):
        self.client = ferrari

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online in ban channel')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def banChannel(self, ctx, channel:discord.TextChannel = None, *, reason=None):
        guild = ctx.guild
        channels = await guild.fetch_channels()
        role_id = 752746015412584538
        role_wicksters = get(guild.roles, id=role_id)
        role_3000 = get(guild.roles, id=758331987324436522)
        role_mods = get(guild.roles, id=748807052440109057)
        role_admin = get(guild.roles, id=783748057351192626)
        role_trial = get(guild.roles, id=864528000418578473)
        channel2 = discord.utils.get(channels, id=844527629057916928)
        embedBan = discord.Embed(title='The following channel was banned or restricted.', description='See below.', color=0xcc0000)
        embedBan.set_author(name=f'Moderator: {ctx.author.name}')
        embedBan.add_field(name=f'{channel.name} was banned.', value=f'Reason: {reason}')
        await channel.set_permissions(role_trial, view_channel=True)
        await channel.set_permissions(role_admin, view_channel=True)
        await channel.set_permissions(role_mods, view_channel=True)
        await channel.set_permissions(role_3000, view_channel=False)
        await channel.set_permissions(role_wicksters, view_channel=False)
        await channel2.send(embed=embedBan)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unbanChannel(self, ctx, channel:discord.TextChannel = None, *, reason=None):
        guild=ctx.guild
        channels = await guild.fetch.channels()
        role_id = 752746015412584538
        role_wicksters = get(guild.roles, id=role_id)
        role_3000 = get(guild.roles, id=758331987324436522)
        role_mods = get(guild.roles, id=748807052440109057)
        role_admin = get(guild.roles, id=783748057351192626)
        role_trial = get(guild.roles, id=864528000418578473)
        channel2 = discord.utils.get(channels, id= 844527629057916928)
        embedUnban = discord.Embed(title='The following channel was unbanned or unrestricted.',description='See below.',color=0x0000FF)
        embedUnban.set_author(name=f'Moderator: {ctx.author.name}')
        embedUnban.add_field(name=f'{channel.name} was unbanned.',value=f'Reason: {reason}')
        await channel.set_permissions(role_trial, view_channel=True)
        await channel.set_permissions(role_admin, view_channel=True)
        await channel.set_permissions(role_mods, view_channel=True)
        await channel.set_permissions(role_3000, view_channel=True)
        await channel.set_permissions(role_wicksters, view_channel=True)
        await channel2.send(embed=embedUnban)


async def setup(ferrari):
    await ferrari.add_cog(banChannel(ferrari))