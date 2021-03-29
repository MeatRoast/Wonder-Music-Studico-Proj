import discord
from discord.ext import commands
import urllib
import urllib.parse
import json
import asyncio
import random
import asyncio
import psutil
import pybithumb
from discord.ext import commands
from datetime import datetime


class _help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="명령어", aliases=['help', '도움말', 'commands'])
    async def _help(self, ctx):
        embedhelp=(
            discord.Embed(
                title="WaterLand-Proj 도움말", 
                description="WaterLand-Proj help",
                color=0xabcee9
            )
            .add_field(
                name=";명령어 기타",
                value="기타 추가된 명령어를 확인 할 수 있습니다."
            )
        )
        if ctx.invoked_subcommand is None:
            await ctx.send(
                embed=embedhelp
            )

        