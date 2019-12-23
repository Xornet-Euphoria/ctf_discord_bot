import discord
from bot_token import TOKEN


client = discord.Client()


@client.event
async def on_ready():
    print(client.user)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "hello":
        await message.channel.send("hahaha")

client.run(TOKEN)