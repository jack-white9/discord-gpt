import os
import discord
from discord.ext import commands
from discord import ClientException
from dotenv import load_dotenv
from src.GptWrapper import GptWrapper

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    try:
        await client.add_cog(GptWrapper(client))
        print(f'{client.user} has connected to Discord successfully')
    except ClientException as e:
        print(f'Failed to connect: {e}')


@client.command()
async def ping(ctx):
    print('ping')
    latency = client.latency
    await ctx.send(latency)

client.run(discord_token)
