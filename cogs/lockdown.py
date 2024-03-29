import discord
from discord import client
from discord.client import Client
from discord.ext import commands
from discord.utils import get


class lockdown(commands.Cog):

    def __init__(self, mercedes):
        self.client = mercedes

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online in Lockdown')

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def lockdown(self , ctx):
        guild = ctx.guild
        channels = await guild.fetch_channels()
        await ctx.send("Lockdown Initiated")
        role_wicksters = get(guild.roles, id=752746015412584538)
        intro = discord.utils.get(channels, id=784145348846944256)
        await intro.set_permissions(role_wicksters,view_channel=False)
        general = discord.utils.get(channels, id=748798206816813121)
        await general.set_permissions(role_wicksters,view_channel=False)
        gaming = discord.utils.get(channels, id=749145111635427429)
        await gaming.set_permissions(role_wicksters,view_channel=False)
        global_chat = discord.utils.get(channels, id=853901384511914004)
        await global_chat.set_permissions(role_wicksters,view_channel=False)
        yt_sug = discord.utils.get(channels, id=755062206697308201)
        await yt_sug.set_permissions(role_wicksters,view_channel=False)
        game_sug = discord.utils.get(channels, id=842712964909629460)
        await game_sug.set_permissions(role_wicksters,view_channel=False)
        feedback = discord.utils.get(channels, id=842713610950410240)
        await feedback.set_permissions(role_wicksters,view_channel=False)
        media = discord.utils.get(channels, id=760348433881366559)
        await media.set_permissions(role_wicksters,view_channel=False)
        art = discord.utils.get(channels, id=796047822792425502)
        await art.set_permissions(role_wicksters,view_channel=False)
        pets = discord.utils.get(channels, id=750926668268306557)
        await pets.set_permissions(role_wicksters,view_channel=False)
        food = discord.utils.get(channels, id=750926641865424997)
        await food.set_permissions(role_wicksters,view_channel=False)
        fun_bots = discord.utils.get(channels, id=753276296892514444)
        await fun_bots.set_permissions(role_wicksters,view_channel=False)
        bot_stuff = discord.utils.get(channels, id=750923873461207140)
        await bot_stuff.set_permissions(role_wicksters,view_channel=False)
        poke = discord.utils.get(channels, id=758209125862998029)
        await poke.set_permissions(role_wicksters,view_channel=False)
        birth = discord.utils.get(channels, id=857570420009730078)
        await birth.set_permissions(role_wicksters,view_channel=False)
        confess = discord.utils.get(channels, id=836845077745500170)
        await confess.set_permissions(role_wicksters,view_channel=False)
        vc = discord.utils.get(channels, id=748844100547248139)
        await vc.set_permissions(role_wicksters,view_channel=False)
        await ctx.send('Lockdown Completed')

    @commands.command(aliases=['Lockdown off', 'unlockdown'])
    @commands.has_permissions(manage_roles=True)
    async def unlock(self, ctx):
        guild = ctx.guild
        await ctx.send("Unlock Initiated")
        channels = await guild.fetch_channels()
        role_wicksters = get(guild.roles, id=752746015412584538)
        intro = discord.utils.get(channels, id=784145348846944256)
        await intro.set_permissions(role_wicksters,view_channel=True)
        general = discord.utils.get(channels, id=748798206816813121)
        await general.set_permissions(role_wicksters,view_channel=True)
        gaming = discord.utils.get(channels, id=749145111635427429)
        await gaming.set_permissions(role_wicksters,view_channel=True)
        global_chat = discord.utils.get(channels, id=853901384511914004)
        await global_chat.set_permissions(role_wicksters,view_channel=True)
        yt_sug = discord.utils.get(channels, id=755062206697308201)
        await yt_sug.set_permissions(role_wicksters,view_channel=True)
        game_sug = discord.utils.get(channels, id=842712964909629460)
        await game_sug.set_permissions(role_wicksters,view_channel=True)
        feedback = discord.utils.get(channels, id=842713610950410240)
        await feedback.set_permissions(role_wicksters,view_channel=True)
        media = discord.utils.get(channels, id=760348433881366559)
        await media.set_permissions(role_wicksters,view_channel=True)
        art = discord.utils.get(channels, id=796047822792425502)
        await art.set_permissions(role_wicksters,view_channel=True)
        pets = discord.utils.get(channels, id=750926668268306557)
        await pets.set_permissions(role_wicksters,view_channel=True)
        food = discord.utils.get(channels, id=750926641865424997)
        await food.set_permissions(role_wicksters,view_channel=True)
        fun_bots = discord.utils.get(channels, id=753276296892514444)
        await fun_bots.set_permissions(role_wicksters,view_channel=True)
        bot_stuff = discord.utils.get(channels, id=750923873461207140)
        await bot_stuff.set_permissions(role_wicksters,view_channel=True)
        poke = discord.utils.get(channels, id=758209125862998029)
        await poke.set_permissions(role_wicksters,view_channel=True)
        birth = discord.utils.get(channels, id=857570420009730078)
        await birth.set_permissions(role_wicksters,view_channel=True)
        confess = discord.utils.get(channels, id=836845077745500170)
        await confess.set_permissions(role_wicksters,view_channel=True)
        vc = discord.utils.get(channels, id=748844100547248139)
        await vc.set_permissions(role_wicksters,view_channel=True)
        await ctx.send('Unlock Completed')

async def setup(mercedes):
    await mercedes.add_cog(lockdown(mercedes))