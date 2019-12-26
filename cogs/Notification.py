from datetime import datetime, timezone, timedelta
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

    print("[+]: request link: {}".format(target))
    req = requests.get(target, headers=header)

    if req.status_code != 200:
        # todo: error handling
        print("[+]: error occured. Status code is {}".format(req.status_code))
        return

    return json.loads(req.text)


def date_format(date_string):
    jst = timezone(timedelta(hours=9))
    date_from_iso = datetime.fromisoformat(date_string)
    new_date = date_from_iso.astimezone(jst)
    return new_date.strftime("%Y-%m-%d(%a) %H:%M:%S")


def cut_time_from_datetime(dt):
    year = dt.year
    month = dt.month
    day = dt.day

    return datetime(year, month, day)


class Notification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def next(self, ctx, *args):
        if len(args) == 0:
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
            url = ctf_data["url"]
            start = date_format(ctf_data["start"])
            finish = date_format(ctf_data["finish"])

            msg = "title:\n\t{}\nurl:\n\t{}\ndate(JST):\n\t{} ~ {}".format(title, url, start, finish)

            await ctx.send(msg)


    @commands.command()
    async def today(self, ctx):
        today_datetime = cut_time_from_datetime(datetime.today()) + timedelta(hours=9)
        api_args = {
            "limit": 10,
            "start": int(today_datetime.timestamp()),
            "finish": int((today_datetime + timedelta(hours=24)).timestamp())
        }

        ctfs = get_event_api(api_args)

        if len(ctfs) == 0:
            await ctx.send("No CTFs will be held today")

        for ctf_data in ctfs:
            msg = "-" * 100
            msg += "\n"
            title = ctf_data["title"]
            url = ctf_data["url"]
            start = date_format(ctf_data["start"])
            finish = date_format(ctf_data["finish"])

            msg += "title:\n\t{}\nurl:\n\t{}\ndate(JST):\n\t{} ~ {}".format(
                title, url, start, finish)

            await ctx.send(msg)

            if len(ctfs) != 0:
                await ctx.send("-" * 100)

    
    @commands.command()
    async def week(self, ctx):
        today_datetime = cut_time_from_datetime(
            datetime.today()) + timedelta(hours=9)
        api_args = {
            "limit": 10,
            "start": int(today_datetime.timestamp()),
            "finish": int((today_datetime + timedelta(days=7)).timestamp())
        }

        ctfs = get_event_api(api_args)

        if len(ctfs) == 0:
            await ctx.send("No CTFs will be held this week")

        for ctf_data in ctfs:
            msg = "-" * 100
            msg += "\n"
            title = ctf_data["title"]
            url = ctf_data["url"]
            start = date_format(ctf_data["start"])
            finish = date_format(ctf_data["finish"])

            msg += "title:\n\t{}\nurl:\n\t{}\ndate(JST):\n\t{} ~ {}\n".format(
                title, url, start, finish)

            await ctx.send(msg)

        if len(ctfs) != 0:
            await ctx.send("-" * 100)
