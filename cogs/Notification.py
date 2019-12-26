from discord.ext import commands, tasks
import requests
import json


def get_event_api(args):
    target = "https://ctftime.org/api/v1/events/?limit={}&start={}&finish={}"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0"
    }
    
    limit = None
    start = None
    finish = None
    if "limit" in args.keys():
        limit = args["limit"]

    if "start" in args.keys():
        start = args["start"]

    if "finish" in args.keys():
        finish = args["finish"]

    target = target.format(limit, start, finish)

    req = requests.get(target, headers=header)

    if req.status_code != 200:
        # todo: error handling
        return

    return json.loads(req.text)


class Notification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def next(self, ctx, *args):
        if len(args) == 0:
            # そのうち複数対応にするかもしれないのでこうしてる
            limit = 1
        else:
            if args[0].isdecimal():
                limit = args[0]
            else:
                limit = 1

        api_args = {
            "limit": limit
        }

        ctfs = get_event_api(api_args)

        for ctf_data in ctfs:
            title = ctf_data["title"]
            desc = ctf_data["description"]
            url = ctf_data["url"]
            start = ctf_data["start"]
            finish = ctf_data["finish"]

            msg = "title: {}\ndescription: {}\nurl: {}\ndate: {} ~ {}".format(title, desc, url, start, finish)

            await ctx.send(msg)

