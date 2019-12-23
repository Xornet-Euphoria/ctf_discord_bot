import discord
from discord.ext import commands
from bot_token import TOKEN


class CTFTools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("login")

    @commands.Cog.listener()
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.bot.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')


if __name__ == "__main__":
    bot = commands.Bot(command_prefix="!")
    bot.add_cog(CTFTools(bot))

    bot.run(TOKEN)
