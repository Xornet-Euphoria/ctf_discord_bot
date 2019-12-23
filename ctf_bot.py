import discord
from discord.ext import commands
from bot_token import TOKEN
import base64


class CTFTools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("login")


    @commands.command()
    async def base64(self, ctx, mode, arg):
        flag = ""

        if mode == "-e":
            flag = base64.b64encode(arg.encode("utf-8")).decode("utf-8")
        elif mode == "-d":
            flag = base64.b64decode(arg.encode("utf-8")).decode("utf-8")
        else:
            await ctx.send("option `mode` must be `-e` or `-d`")
            return
        await ctx.send(flag)


if __name__ == "__main__":
    bot = commands.Bot(command_prefix="!")
    bot.add_cog(CTFTools(bot))

    bot.run(TOKEN)
