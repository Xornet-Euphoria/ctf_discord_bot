from discord.ext import commands
from bot_token import TOKEN
from cogs.CTFTools import *


if __name__ == "__main__":
    bot = commands.Bot(command_prefix="!")
    bot.add_cog(CTFTools(bot))

    bot.run(TOKEN)
