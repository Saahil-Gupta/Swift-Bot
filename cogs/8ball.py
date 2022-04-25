import discord
from discord.client import Client
from discord.ext import commands
from discord.ext.commands import bot
import random

class eightball(commands.Cog):

    def __init__(self, bots):
        self.client = bots

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online in 8ball')

    @commands.command(aliases=['8ball', 'eightball'])
    async def _8ball(self, ctx, *,question):
        responses = ['It is Certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Dont count on it.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful. ']
        await ctx.send(f'Questions: {question}\nAnswer: {random.choice(responses)}')

async def setup(bots):
    await bots.add_cog(eightball(bots))