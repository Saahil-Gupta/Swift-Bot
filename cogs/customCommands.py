import discord
from discord.client import Client
from discord.ext import commands
from discord.ext.commands import bot


class Custom(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online in the Custom Commands')

    @commands.command()
    async def instagram(self, ctx):
        await ctx.send('Follow Julia on Instagram: http://instagram.com/juliaaburch')

    @commands.command(aliases=['Instagram'])
    async def clay(self, ctx):
        await ctx.send("Clay is always High.")

    @commands.command(aliases=['Snapchat'])
    async def snapchat(self, ctx):
        await ctx.send("Add Julia on Snapchat: julia.burch")

    @commands.command(aliases=['Twitter'])
    async def twitter(self, ctx):
        await ctx.send("Follow Julia on Twitter http://twitter.com/juliaaburch")

    @commands.command(aliases=['Youtube'])
    async def youtube(self, ctx):
        await ctx.send("Follow Julia on YouTube http://youtube.com/juliaburch")

    @commands.command(aliases=['Donate'])
    async def donate(self, ctx):
        await ctx.send("Wanna support Julia? Donate here: https://streamlabs.com/juliaburch/tip")

    @commands.command(aliases=['Socials'])
    async def socials(self, ctx):
        await ctx.send("Instagram http://instagram.com/juliaaburch\nYoutube-https://youtube.com/juliaburch\nTwitter-"
                       "http"
                       "://twitter.com/JuliaaBurch\nTikTok- https://vm.tiktok.com/CWeb3A/\nSnapchat-julia.burch\nFace"
                       "book-https://www.facebook.com/juliaaburchh")

    @commands.command(aliases=['Twitch'])
    async def twitch(self, ctx):
        await ctx.send("Follow Julia on Twitch! https://www.twitch.tv/juliaburch")

    @commands.command(aliases=['Twinchannel', 'TwinChannel'])
    async def twinchannel(self, ctx):
        await ctx.send("Follow their twin YouTube channel! https://www.youtube.com/channel/UCLJ8NEz9OeUmXOnItUfUBRQ/"
                       "featured")

    @commands.command(aliases=['Gamingchannel', 'GamingChannel'])
    async def gamingchannel(self, ctx):
        await ctx.send("Julia's Gaming channel! https://www.youtube.com/channel/UCigOCMIzDMXGJXtGOQZv6xA")

    @commands.command(aliases=['TikTok'])
    async def tiktok(self, ctx):
        await ctx.send("Follow Julia on TikTok! https://tiktok.com/@julia.burch?lang=eng")


def setup(client):
    client.add_cog(Custom(client))
