from discord.ext import commands, tasks
import requests
import json


class Notification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def next(self, ctx, *args):
        target = "https://ctftime.org/api/v1/events/?limit={}"
        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0"
        }

        if len(args) == 0:
            # そのうち複数対応にするかもしれないのでこうしてる
            limit = 1
        
        req = requests.get(target.format(limit), headers=header)

        if req.status_code != 200:
            await ctx.send("[+]: an error occurred. Status code: {}".format(req.status_code))
            return

        ctf_data = json.loads(req.text)[0]

        title = ctf_data["title"]
        desc = ctf_data["description"]
        url = ctf_data["url"]
        start = ctf_data["start"]
        finish = ctf_data["finish"]

        msg = "title: {}\ndescription: {}\nurl: {}\ndate: {} ~ {}".format(title, desc, url, start, finish)

        await ctx.send(msg)

