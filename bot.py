import os
import discord
from discord import ClientException
from dotenv import load_dotenv
from src.GptWrapper import GptWrapper

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    try:
        await client.add_cog(GptWrapper(client))
        print(f'{client.user} has connected to Discord successfully')
    except ClientException as e:
        print(f'Failed to connect: {e}')

client.run(discord_token)
