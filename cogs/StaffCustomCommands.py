import discord
from discord.client import Client
from discord.ext import commands

class StaffCustomCommands(commands.Cog):

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

    @commands.command()
    async def shyboy(self, ctx):
        await ctx.send("They don't call me the funny cute handsome mod for nothing!")

    @commands.command()
    async def bear(self, ctx):
        await ctx.send("He is Big! He is Strong! He is Super Cool and Hot! I-i-i-i-it's Bear!")

    @commands.command()
    async def duffstuff(self, ctx):
        await ctx.send("'He takes all the fun out of modding and chess' - Cullen FeelsBadMan")

    @commands.command()
    async def bbm(self, ctx):
        await ctx.send("https://www.twitch.tv/brutalbearman")

    @commands.command()
    async def sahara(self, ctx):
        await ctx.send("'One mans cringe is another mans PogChamp' -Sahara 2021")

    @commands.command()
    async def ashisfine1(self, ctx):
        await ctx.send("Ash is the twin that was watching a twin but now is modding as a twin for that twin that the twin was watching.")

    @commands.command()
    async def duff(self, ctx):
        await ctx.send("He is a robot and also Streamlabs brother")

    @commands.command()
    async def bigbrainash(self, ctx):
        await ctx.send("Sometimes Ash can be smart but only sometimes")

    @commands.command()
    async def sahara1(self, ctx):
        await ctx.send("Sahara streams with Julia on fridays! Check her out at https://www.twitch.tv/SaharaNotTheDesert :)")
       
    @commands.command(aliases=['Coronor', 'pilotsnow', 'coronor'])
    async def Pilotsnow(self, ctx):
        await ctx.send("She is Fun and Intoxicating. Beware !")

def setup(swift):
    swift.add_cog(StaffCustomCommands(swift))
