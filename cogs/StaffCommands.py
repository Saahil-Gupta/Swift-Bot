import discord
from discord.client import Client
from discord.ext import commands
from discord.ext.commands import bot

class StaffCommands(commands.Cog):

    def __init__(self, swift):
        self.client = swift

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online in Staff Commands')

    @commands.command()
    async def archangel3(self, ctx):
        await ctx.send("archangel is the best admin to exist! (yea better than clay)")

    @commands.command(aliases=['Darth'])
    async def darth(self, ctx):
        await ctx.send("This wondeful bot was made by our own mod: DarthBlack")

    @commands.command()
    async def mck(self, ctx):
        await ctx.send("mck is tall and will step on you")

    @commands.command(aliases=['7amadi'])
    async def _7amadi(self, ctx):
        await ctx.send("amadi is THE weirdo, simps for possibly everyone around him.")

    @commands.command()
    async def archangel2(self, ctx):
        await ctx.send("You know what they say?.... He who hesitates, disintegrates!")

    @commands.command()
    async def rollo(self, ctx):
        await ctx.send("has a very oversized brain")

    @commands.command()
    async def nicolas(self, ctx):
        await ctx.send("If you have a question about memes or Pokémon, he is your man")

    @commands.command()
    async def theogbrownie(self, ctx):
        await ctx.send("If you need song lyric spam, then TheOGBrownie is your mod!")

    @commands.command()
    async def ashisfine(self, ctx):
        await ctx.send("On the 24/03/21 I banned my first person!")

    @commands.command()
    async def alex(self, ctx):
        await ctx.send("Is he actually called Alex? Because the name is aiex. I am confuse. :S")

    @commands.command()
    async def cullen(self, ctx):
        await ctx.send("Will he be a mod? YES HE WILL! Twitch heard that he couldn't gamble anymore, so made it that he CAN! monkaS")

    @commands.command()
    async def kingpanda(self, ctx):
        await ctx.send("KingPanda may be young, but he learns quickly and his sword is just as sharp!")

    @commands.command()
    async def archangel(self, ctx):
        await ctx.send("Less than 3! <3")

    @commands.command(aliases=['Gabe'])
    async def gabe(self, ctx):
        await ctx.send("Gabe the Babe is the noicest person in the server.")


def setup(swift):
    swift.add_cog(StaffCommands(swift))