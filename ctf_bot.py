import discord
from bot_token import TOKEN

client = discord.Client()

@client.event
async def ready():
    print(client.user)

client.run(TOKEN)