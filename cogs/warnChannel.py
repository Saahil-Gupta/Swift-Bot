import discord
from discord import client
from discord.client import Client
from discord.ext import commands
from discord import Emoji
from discord.utils import get

class warnChannel(commands.Cog):

    def __init__(self, darth):
        self.client = darth

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online in warn channel')

    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def warnChannel(self, ctx, user: discord.User, *, reason=None):
        guild = ctx.guild
        channels = await guild.fetch_channels()
        channel2 = discord.utils.get(channels, id=844527629057916928)
        role_id = 752746015412584538
        role_wicksters = get(guild.roles, id=role_id)
        role_3000 = get(guild.roles, id=758331987324436522)
        role_mods = get(guild.roles, id=748807052440109057)
        role_admin = get(guild.roles, id=783748057351192626)
        role_trial = get(guild.roles, id=864528000418578473)
        overwrites={
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            guild.me: discord.PermissionOverwrite(view_channel=True),
            user: discord.PermissionOverwrite(view_channel=True),
            role_wicksters: discord.PermissionOverwrite(view_channel=False),
            role_3000: discord.PermissionOverwrite(view_channel=False),
            role_trial: discord.PermissionOverwrite(view_channel=True),
            role_mods: discord.PermissionOverwrite(view_channel=True),
            role_admin: discord.PermissionOverwrite(view_channel=True)
        }
        embedMod = discord.Embed(title = 'Information for the mods', description = '!jbclose [channel ID]- Closes the text channel'
                                                                                   '\n!jbhistory-To make a log of the conversation in the warn channel(This Command is still WIP). Send the txt file to the logs.\n If the issue was resolved, That is Amazing. If it could not be resolved,'
                                                                                   'Send the reason of the issue not being resolved in #Punishments', color = 0x00FF00)

        embedCha = discord.Embed(title='🧨A new Warn Channel was created🧨', decription='Warn Channel', color=0xcccc00)
        embedCha.set_author(name=user.display_name, icon_url=user.avatar_url)
        embedCha.set_thumbnail(url=user.avatar_url)
        embedCha.add_field(name=f'Moderator:{ctx.author.name}', value=f'{user.id} is the ID of the person for whom the warn channel was made.\n Reason: {reason}')

        embedUser= discord.Embed(title=f"Information for the Warned person-{user}", description='You are being warned! So listen closely to the staff and show some respect.', color=0xFFC1E6)

        channel_warn = await guild.create_text_channel(name=f'{user.name}-warn', overwrites=overwrites)
        await channel2.send(embed=embedCha)
        await channel_warn.send(embed=embedMod)
        await channel_warn.send(embed=embedUser)
        await channel_warn.send(f'{user.mention} Please come here.')

    @warnChannel.error
    async def warnChannel_error(self, ctx, error):
        guild = ctx.guild
        channels = await guild.fetch_channels()
        channel2 = bot.get_channel(844527629057916928)
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{ctx.message.author.mention} You do not have the permission to run that command! :red_circle:')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{ctx.message.author.mention} There is an Argument missing in that command! :red_circle:\nWarn Channel Syntax: ```!jbwarnChannel [@user or ID] [reason]```')
        elif isinstance(error, commands.BadArgument):
            await ctx.send(f'{ctx.message.author.mention} To mute someone you need to mention them! :red_circle:\nWarn Channel Syntax: ```!jbwarnChannel [@user or ID] [reason]```')
        else:
            await ctx.send('There was an error while executing the command! DarthBlack has been informed! :red_circle:')
            await channel2.send('There was an error while executing the command! DarthBlack has been informed! :red_circle:')
            print(error)


def setup(darth):
    darth.add_cog(warnChannel(darth))
