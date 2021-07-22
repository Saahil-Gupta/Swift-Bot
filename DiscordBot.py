import discord
import os
from discord.ext import commands
from discord.utils import get
from discord import Embed, DMChannel, Role, Attachment

bot = commands.Bot(command_prefix='!jb')

# ----------------------------------------------------------------------------------------------


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='DM to Contact Staff | !jbhelp'))
    print('Bot is online and Ready to Go')


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
    mbed.add_field(name=' This Modmail has been closed', value='Mods tag this embed and send the reason/situation for'
                                                               ' which a member used modmail. Send it below this embed')
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
    embedMod = discord.Embed(title = 'Information for the mods', description = '!close [channel ID]- Closes the text channel'
                                                                               '\n!export- to make a log of the warn channel. It will be exported as a .txt file. Send the txt file to the logs.\n If the issue was resolved, That is Amazing. If it could not be resolved,'
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


@bot.command()
async def julia(ctx):
    await ctx.send('Julia is from Ontario and streams on Twitch! You should check her out at https://www.twitch.tv/juliaburch.')


@bot.command()
async def bear(ctx):
    await ctx.send("He is Big! He is Strong! He is Super Cool and Hot! I-i-i-i-it's Bear!")


@bot.command()
async def vibecheck(ctx):
    await ctx.send("The vibe is cool and balanced.")


@bot.command()
async def duffstuff(ctx):
    await ctx.send("'He takes all the fun out of modding and chess' - Cullen FeelsBadMan")


@bot.command()
async def bbm(ctx):
    await ctx.send("https://www.twitch.tv/brutalbearman")


@bot.command()
async def sahara(ctx):
    await ctx.send("'One mans cringe is another mans PogChamp' -Sahara 2021")


@bot.command()
async def farts(ctx):
    await ctx.send("Turns out that Carter's farts smell good. So if you get the chance then give them a sniff.")



@bot.command()
async def squids(ctx):
    await ctx.send("Julia loves them. They are just the best thing in minecraft. So derpy and cute!")


@bot.command()
async def gam(ctx):
    await ctx.send("RIP GoldenArmourMan He fought well and taught Julia how to parry. F.")


@bot.command()
async def ashisfine1(ctx):
    await ctx.send("Ash is the twin that was watching a twin but now is modding as a twin for that twin that the twin was watching.")


@bot.command()
async def dolphinmurder1(ctx):
    await ctx.send("https://clips.twitch.tv/AthleticToughPanPRChase-pCUoTSeMH6JiJDt_")


@bot.command()
async def dolphinmurder2(ctx):
    await ctx.send("https://clips.twitch.tv/DeadAstuteKimchiOhMyDog-Fq8ouAqci6X1xJE7")


@bot.command()
async def duff(ctx):
    await ctx.send("He is a robot and also Streamlabs brother")


@bot.command()
async def bigbrainash(ctx):
    await ctx.send("Sometimes Ash can be smart but only sometimes")


@bot.command()
async def pog(ctx):
    await ctx.send("it truly is POG")


@bot.command()
async def becool(ctx):
    await ctx.send("Wanna be cool? Here's how: \nCOOL TIER 1: Watch her streams. COOL TIER 2: Sub to her twitch. SWAG TIER 1: Sub to her YT. SWAG TIER 2: Join YT membership. POGCHAMP 1: Join her discord POGCHAMP 2: Worship the wick religion")


@bot.command()
async def wickreligion(ctx):
    await ctx.send(f'"hou shall worship the wick to be the wicked, what is our motto? "Whoever comes, whoever it is...we kill em", what do we need? "Guns. Lots of guns." We work in the dark to serve the light! WE ARE THE WICKSTERS!! <:PowerUpL:857613184479002645><:juliab3Wick:857613184479002645><:PowerUpR:857613184479002645>')


@bot.command()
async def lady(ctx):
    await ctx.send("The WHOLE chat has a crush on Lady Dimitrescu (Except from Ash)")


@bot.command()
async def monitor(ctx):
    await ctx.send("Julia has a monitor, also another monitor. They are known as monitor 1 and monitor 2.")


@bot.command()
async def julesapology(ctx):
    await ctx.send('"I am so sorry" *continues shooting it*')


@bot.command()
async def juliaiscarter(ctx):
    await ctx.send("https://clips.twitch.tv/LongCuteHamsterLitty-hnUBK7w1wD35polv")


@bot.command()
async def sahara1(ctx):
    await ctx.send("Sahara streams with Julia on fridays! Check her out at https://www.twitch.tv/SaharaNotTheDesert :)")


@bot.command()
async def whereislauren(ctx):
    await ctx.send("its always where is lauren but never how is lauren FeelsBadMan")

# -------------------------------------------------------------------------------------------

bot.run(os.environ['token'])
