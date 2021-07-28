import discord
from discord import client
from discord.client import Client
from discord.ext import commands

class MiscCommands(commands.Cog):

    def __init__(self, sheeran):
        self.client = sheeran

    @commands.command()
    async def vibecheck(self, ctx):
        await ctx.send("The vibe is cool and balanced.")

    @commands.command()
    async def pog(self, ctx):
        await ctx.send("it truly is POG")

    @commands.command()
    async def becool(self, ctx):
        await ctx.send("Wanna be cool? Here's how: \nCOOL TIER 1: Watch her streams. COOL TIER 2: Sub to her twitch. SWAG TIER 1: Sub to her YT. SWAG TIER 2: Join YT membership. POGCHAMP 1: Join her discord POGCHAMP 2: Worship the wick religion")

    @commands.command()
    async def wickreligion(self, ctx):
        await ctx.send(f'"hou shall worship the wick to be the wicked, what is our motto? "Whoever comes, whoever it is...we kill em", what do we need? "Guns. Lots of guns." We work in the dark to serve the light! WE ARE THE WICKSTERS!! <:PowerUpL:857613184479002645><:juliab3Wick:857613184479002645><:PowerUpR:857613184479002645>')

    @commands.command()
    async def lady(self, ctx):
        await ctx.send("The WHOLE chat has a crush on Lady Dimitrescu (Except from Ash)")

    @commands.command()
    async def farts(self, ctx):
        await ctx.send("Turns out that Carter's farts smell good. So if you get the chance then give them a sniff.")

    @commands.command()
    async def squids(self, ctx):
        await ctx.send("Julia loves them. They are just the best thing in minecraft. So derpy and cute!")

    @commands.command()
    async def gam(self, ctx):
        await ctx.send("RIP GoldenArmourMan He fought well and taught Julia how to parry. F.")

    @commands.command()
    async def whereislauren(self, ctx):
        await ctx.send("its always where is lauren but never how is lauren FeelsBadMan")

def setup(sheeran):
    sheeran.add_cog(MiscCommands(sheeran))
