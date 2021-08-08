import discord
import os
from discord.ext import commands
from discord.utils import get
from discord import Embed, DMChannel, Role, Attachment
from discord.abc import GuildChannel, _Overwrites
import asyncio
import datetime as dt
from discord.ext import tasks
import asyncio

bot = commands.Bot(command_prefix='!jb')

# ----------------------------------------------------------------------------------------------


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='DM to Contact Staff | !jbhelp'))
    print('Bot is online and Ready to Go')
    msg1.start()

@tasks.loop(hours=8)
async def msg1():
    message_channel = bot.get_channel(748798206816813121) # • 748798206816813121
    pink_heart = discord.utils.get(bot.emojis, id=859977705406595102)
    pink_butterfly = discord.utils.get(bot.emojis, id=856262693241749525)
    embedAuto = discord.Embed(title=f'{pink_butterfly} Sub Reminder',description=f'\n{pink_heart} TYSM for all the support!\n\n'
    "• Sub to [Julia Burch](https://www.youtube.com/channel/UCcRKWdzb5P9jsswSHmuq9PA)\n"
    "• Sub to [Julia Burch Shorts](https://www.youtube.com/channel/UCpaxSWzKLtS3uY4Gkp-_SOQ)\n"
    "• Sub to [Julia Burch Livestreams](https://www.youtube.com/channel/UCigOCMIzDMXGJXtGOQZv6xA)",color=0xFFC1E6)
    embedAuto.set_thumbnail(url="https://images-ext-2.discordapp.net/external/otj151m1XhrpCs_OUT2SIhBHTXpa4P9hLtZjUOQEWLI/%3Fv%3D1/https/cdn.discordapp.com/emojis/850562956877365298.gif")
    await message_channel.send(embed=embedAuto)


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! \n Latency: {bot.latency * 1000}ms')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if isinstance(message.channel, DMChannel):
        guild = bot.get_guild(748798206816813117)
        channels = await guild.fetch_channels()
        channel2 = bot.get_channel(844527629057916928)  # for modmail log
        # searched_role = get.guild.roles(id=856759954630770699)
        role_discordmod = discord.utils.get(guild.roles, id=839881498961641483)
        role_id = 752746015412584538
        role_wicksters = get(guild.roles, id=role_id)
        role_3000 = get(guild.roles, id=758331987324436522)
        role_mods = get(guild.roles, id=748807052440109057)
        role_admin = get(guild.roles, id=783748057351192626)
        role_trial = get(guild.roles, id=864528000418578473)
        channel = discord.utils.get(channels, name=str(message.author.id))

        # Embed for the user message
        embedVar = discord.Embed(title=f'{message.author} has sent a new message', description=message.content,
                                 color=0xFFC1E6)
        embedVar.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)

        # Embed sent to the user
        embedDM = discord.Embed(title='A new thread has been created', description='A staff member will be with you '
                                                                                   'shortly.Please be patient and wait'
                                                                                   'for their response.'
                                , color=0xFFC1E6)
        embedDM.add_field(name='Repeat', value='Please repeat your problem again. Send the first message again')
        embedDM.add_field(name='Image', value='To send an image, \n 1) send the image in this chat.\n 2) '
                                              'Copy the image link.\n 3) Paste the image link in this chat. '
                                              'You are done :)')
        embedDM.add_field(name='Link', value='To send a link, just paste the link in the chat.')

        # Embed for the mods
        embedMod = discord.Embed(title='Information for the mods', description='!jbclose [Channel ID]- Closes the text channel'
                                                                                '\n!jbDM @user [message]- '
                                                                               'To DM the user anonymously \n'
                                                                                'Mods should remember that any message '
                                                                                'under 5 characters will not be sent.'
                                                                               ' Please '
                                                                                'make sure that its not less than 5 '
                                                                               'characters', color=0x00FF00)

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            guild.me: discord.PermissionOverwrite(read_messages=True),
            role_wicksters: discord.PermissionOverwrite(view_channel=False),
            role_3000: discord.PermissionOverwrite(view_channel=False),
            role_mods: discord.PermissionOverwrite(view_channel=True),
            role_trial: discord.PermissionOverwrite(view_channel=True),
            role_admin: discord.PermissionOverwrite(view_channel=True)
        }
        # Embed to be sent to modmail log when a new channel si created
        embedCha = discord.Embed(title='🎐A new Channel was created🎐', decription=message.author.id, color=0xFFC1E6)
        embedCha.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)
        embedCha.set_thumbnail(url=bot.user.avatar_url)
        embedCha.add_field(name='Mods please help the above mentioned person. The ID of the person is given below', value=message.author.id)

        if channel is None:
            await message.author.send(embed=embedDM)

            await guild.create_text_channel(name=str(message.author.id), overwrites=overwrites)
            # category = category)
            await channel2.send(embed=embedCha)
            await channel2.send(f'{role_discordmod.mention} A new Modmail Channel has been created')
        elif channel is not None:
            await channel.send(embed=embedMod)
            await channel.send(embed=embedVar)
        if len(message.attachments) > 0:
            await channel.send(str(message.attachments))

        # await channel.send(embed=embedVar)

    await bot.process_commands(message)


@bot.command(description='Used to DM the user/member through the bot', aliases=['DM'])
@commands.has_permissions(manage_messages=True)
async def dm(ctx, user: discord.User, *, message=None):
    embedVarr = discord.Embed(title='Moderators have sent a new message', description=message or "This Message is"
                                                                                                 " sent via DM",
                              color=0xFFC1E6)
    await user.send(embed=embedVarr)


@bot.command()
@commands.has_guild_permissions(manage_messages=True)
async def close(ctx, channel: discord.TextChannel):
    mbed = discord.Embed(title='Success',
                         description=f'Channel: {ctx.channel.name} has been deleted')
    mbed.add_field(name=' This Modmail/Warn Channel has been closed', value='Mods tag this embed and send the reason/situation for'
                                                               ' which a member used modmail or you made a warn channel. Send it below this embed')
    channel = bot.get_channel(844527629057916928)

    await channel.send(embed=mbed)
    await ctx.channel.delete()

# --------------------------------------------------------------------------------------------
@bot.command()
@commands.has_guild_permissions(manage_messages=True)
async def warnChannel(ctx, user: discord.User, *, reason=None):
    guild = ctx.guild
    channels = await guild.fetch_channels()
    channel2 = bot.get_channel(844527629057916928)
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

#
# @bot.command()
# async def history(ctx):
#     channel2 = bot.get_channel(864724149079244830)
#     async for msg in ctx.channel.history(limit=None):
#         embedHis=discord.Embed(title='Message History of Warn Channel',desription=f'{ctx.channel.name}')
#         embedHis.add_field(name=f'Moderator:{ctx.author.name}',value=f"{msg.created_at} - {msg.author.display_name}: {msg.content}\n")
#         await channel2.send(embed=embedHis)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def restrictUser(ctx, user: discord.User, *, Channel:discord.TextChannel= None):
    guild = ctx.guild
    channel2 = bot.get_channel(844527629057916928)
    overwrite1 = discord.PermissionOverwrite()
    overwrite1.view_channel=False
    embedChannel=discord.Embed(title='Person Restricted.', description=f'Restricted the following user: {user.name} ❌', color=0xcc0000)
    embedRestrict=discord.Embed(title=f'Person restricted. User:{user}', description='The following person was banned from the below mentioned channel', color=0xcc0000)
    embedRestrict.add_field(name=f'Moderator:{ctx.author.name}',value=f'Channel: {Channel.name}')
    await Channel.set_permissions(user, overwrite=overwrite1)
    await ctx.channel.send(embed=embedChannel)
    await channel2.send(embed=embedRestrict)


@bot.command()
@commands.has_permissions(manage_messages=True)
async def unrestrict(ctx, user: discord.User, *, Channel:discord.TextChannel= None):
    guild = ctx.guild
    channel2 = bot.get_channel(844527629057916928)
    overwrite2 = discord.PermissionOverwrite()
    overwrite2.view_channel=True
    embedUnrestrict=discord.Embed(title=f'Person unrestricted. User:{user}', description='The following person was unbanned from the below mentioned channel', color=0x8fcc00)
    embedUnrestrict.add_field(name=f'Moderator:{ctx.author.name}',value=f'Channel: {Channel.name}', color=0x8fcc00)
    embedChannel=discord.Embed(title='Person Unrestricted.', description=f'Unrestricted the following user: {user.name} ✅')
    await Channel.set_permissions(user, overwrite=overwrite2)
    await ctx.channel.send(embed=embedChannel)
    await channel2.send(embed=embedUnrestrict)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def banChannel(ctx, channel:discord.TextChannel=None,*,reason=None):
    guild=ctx.guild
    role_id = 752746015412584538
    role_wicksters = get(guild.roles, id=role_id)
    role_3000 = get(guild.roles, id=758331987324436522)
    role_mods = get(guild.roles, id=748807052440109057)
    role_admin = get(guild.roles, id=783748057351192626)
    role_trial = get(guild.roles, id=864528000418578473)
    channel2 = bot.get_channel(844527629057916928)
    embedBan= discord.Embed(title='The following channel was banned or restricted.',description='See below.',color=0xcc0000)
    embedBan.set_author(name=f'Moderator: {ctx.author.name}')
    embedBan.add_field(name=f'{channel.name} was banned.',value=f'Reason: {reason}')
    await channel.set_permissions(role_trial, view_channel=True)
    await channel.set_permissions(role_admin, view_channel=True)
    await channel.set_permissions(role_mods, view_channel=True)
    await channel.set_permissions(role_3000, view_channel=False)
    await channel.set_permissions(role_wicksters, view_channel=False)
    await channel2.send(embed=embedBan)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def unbanChannel(ctx, channel:discord.TextChannel=None, *, reason=None):
    guild=ctx.guild
    role_id = 752746015412584538
    role_wicksters = get(guild.roles, id=role_id)
    role_3000 = get(guild.roles, id=758331987324436522)
    role_mods = get(guild.roles, id=748807052440109057)
    role_admin = get(guild.roles, id=783748057351192626)
    role_trial = get(guild.roles, id=864528000418578473)
    channel2 = bot.get_channel(844527629057916928)
    embedUnban= discord.Embed(title='The following channel was unbanned or unrestricted.',description='See below.',color=0x0000FF)
    embedUnban.set_author(name=f'Moderator: {ctx.author.name}')
    embedUnban.add_field(name=f'{channel.name} was unbanned.',value=f'Reason: {reason}')
    await channel.set_permissions(role_trial, view_channel=True)
    await channel.set_permissions(role_admin, view_channel=True)
    await channel.set_permissions(role_mods, view_channel=True)
    await channel.set_permissions(role_3000, view_channel=True)
    await channel.set_permissions(role_wicksters, view_channel=True)
    await channel2.send(embed=embedUnban)
# -------------------------------------------------------------------------------------------

bot.run(os.environ['token'])
