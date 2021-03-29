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
from selenium import webdriver
import time


class _server(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=['서버'])
    async def _server(self, ctx):
        memory = psutil.virtual_memory()
        avail = round(memory.available/1024**3, 1) #사용 가능한 메모리 계산
        percent = memory.percent #메모리 퍼센트 계산
        total = round(memory.total/1024**3, 1) # 총 메모리를 계산 후 소수점 1자리 까지만 반올림
        distotal = round(memory.total/1024**3) # "" 반올림 (소수점 X)
        embedhelp=(
            discord.Embed(
                title="현재 서버 사용량 입니다.", 
                description="시스템정보",
                color=0xabcee9
            )
            .add_field(
                name="CPU 사용량:",
                value=f"{psutil.cpu_percent()}%",
                inline=False
            )
            .add_field(
                name="메모리 사용량:",
                value=f"{distotal}GB 중 {round(total - avail, 1)}GB 사용 중 ({avail}GB 사용 가능 ({percent}%))",
                inline=False
            )
        )
        await ctx.send(
            embed=embedhelp
        )