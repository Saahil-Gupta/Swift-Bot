import discord
from discord.client import Client
from discord.ext import commands

class StaffCommands(commands.Cog):

    def __init__(self, taylor):
        self.client = taylor

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online in Streamer Commands')

    @commands.command()
    async def ruleswhy1(self, ctx):
        await ctx.send("Moderators can't manage other languages")

    @commands.command()
    async def ruleswhy2(self, ctx):
        await ctx.send('Negativity and hate make a horrible place to be.')

    @commands.command()
    async def ruleswhy3(self, ctx):
        await ctx.send("No need to ping her, she reads the chat if she's free.")

    @commands.command()
    async def ruleswhy4(self, ctx):
        await ctx.send("Being excessively creepy or flirty is not acceptable.")

    @commands.command()
    async def age(self, ctx):
        await ctx.send('Julia is 20 years old.')

    @commands.command()
    async def love(self, ctx):
        await ctx.send('Love yourself and keep it to yourself please!')

    @commands.command()
    async def birthday(self, ctx):
        await ctx.send('07/12/2000 12/07/2000 2000/12/07 2000/07/12 07/2000/12 12/2000/07')

    @commands.command()
    async def carter(self, ctx):
        await ctx.send("Carter is Julia's boyfriend! twitch.tv/cmoney3051")

    @commands.command()
    async def sister(self, ctx):
        await ctx.send("Lauren is my twin sister, she also does not live with me!")

    @commands.command()
    async def height(self, ctx):
        await ctx.send("5ft 3Inch = 160cm")

    @commands.command()
    async def minecraft(self, ctx):
        await ctx.send("The Minecraft Server is a subscriber only server, subscribe on twitch then whisper the streamer with your username. :)")

    @commands.command()
    async def games(self, ctx):
        await ctx.send("Julia is a variety streamer and plays many games. Such as COD, RE, Outlast, Minecraft and many others!")

    @commands.command()
    async def juliaq1(self, ctx):
        await ctx.send("I wasn't teabagging him, I was cuddling him!' - Julia, Phasmophobia 27/02/2021")

    @commands.command()
    async def juliaq2(self, ctx):
        await ctx.send('"He yeeted my bf out the window" - Julia Phasmophobia 27/02/2021')

    @commands.command()
    async def mic(self, ctx):
        await ctx.send("Shure SM7B")

    @commands.command()
    async def camera(self, ctx):
        await ctx.send("Julia uses a camera as a camera. Logitech 1080p.")

    @commands.command()
    async def headset(self, ctx):
        await ctx.send("My headset is the Razer Kraken headset or something like that. OR The Yowu chan .com website or something.")

    @commands.command()
    async def where(self, ctx):
        await ctx.send("Lauren is at her flat check her socials to keep updated")

    @commands.command()
    async def keyboard(self, ctx):
        await ctx.send("AN Pro 2")

    @commands.command()
    async def english(self, ctx):
        await ctx.send("Please keep the chat english only, it helps the Mods to keep this chat a safe and positive place for everyone!")

    @commands.command()
    async def professions(self, ctx):
        await ctx.send("Julia has many professions such as... Burch The Builder, Julia Wick, Professor Burch, Burch The Killer, Sniper Burch, Big Brain Burch, Detective Burch, Julia The Hero, Baker Burch, Power Burch, Panda Murderer Burch and Burch The Dolphin Killer, Murderer Burch, Burch The Bear Blamer, Engineer Burch, Burch Ramsay and Painter Burch")

    @commands.command()
    async def betrayal(self, ctx):
        await ctx.send("https://clips.twitch.tv/ManlyImportantHummingbirdFailFish-E3QzO_UwY1CG7l5V")

    @commands.command(aliases=['Julialivingwithbf'])
    async def julialivingwithbf(self, ctx):
        await ctx.send("I kinda live with my bf, I kinda live alone --Julia 2021")

    @commands.command(aliases=['Family'])
    async def family(self, ctx):
        await ctx.send("It's with the family.")

    @commands.command()
    async def julia(self, ctx):
        await ctx.send('Julia is from Ontario and streams on Twitch! You should check her out at https://www.twitch.tv/juliaburch.')

    @commands.command()
    async def monitor(self, ctx):
        await ctx.send("Julia has a monitor, also another monitor. They are known as monitor 1 and monitor 2.")

    @commands.command()
    async def julesapology(self, ctx):
        await ctx.send('"I am so sorry" *continues shooting it*')

    @commands.command()
    async def juliaiscarter(self, ctx):
        await ctx.send("https://clips.twitch.tv/LongCuteHamsterLitty-hnUBK7w1wD35polv")

    @commands.command()
    async def dolphinmurder1(self, ctx):
        await ctx.send("https://clips.twitch.tv/AthleticToughPanPRChase-pCUoTSeMH6JiJDt_")

    @commands.command()
    async def dolphinmurder2(self, ctx):
        await ctx.send("https://clips.twitch.tv/DeadAstuteKimchiOhMyDog-Fq8ouAqci6X1xJE7")

async def setup(taylor):
    await taylor.add_cog(StaffCommands(taylor))
