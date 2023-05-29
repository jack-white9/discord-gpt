from discord.ext import commands


class GptWrapper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chat(self, ctx):
        ctx.send('Hello, world!')
