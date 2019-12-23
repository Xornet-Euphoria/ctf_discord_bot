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
            await ctx.send("[usage]: !base64 <mode (`-d` or `-e`)> <string>")
            return
        await ctx.send(flag)


    @commands.command()
    async def rot13(self, ctx, *args):
        flag = ""
        if len(args) == 0:
            await ctx.send("[usage]: !rot13 <string> <num (optional)>")
            return
        
        s = args[0]
        if len(args) > 1 and args[1].isdecimal():
            n = int(args[1]) % 26
        else:
            n = 13

        for c in s:
            if 'a' <= c <= 'z':
                flag += chr(((ord(c) - ord('a')) + n) % 26 + ord('a'))
            elif 'A' <= c <= 'Z':
                flag += chr(((ord(c) - ord('A')) + n) % 26 + ord('A'))
            else:
                flag += c

        await ctx.send(flag)


if __name__ == "__main__":
    bot = commands.Bot(command_prefix="!")
    bot.add_cog(CTFTools(bot))

    bot.run(TOKEN)
