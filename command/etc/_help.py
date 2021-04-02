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

    @commands.group(name="명령어", aliases=['help', '도움말', 'commands'])
    async def _help(self, ctx):
        embedhelp=(
            discord.Embed(
                title="Wonder-Music-Studico-Proj 도움말", 
                description="Wonder-Music-Studico-Proj help",
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
    @_help.command(name="기타", aliases=["etc"])
    async def _helpetc(self, ctx):
        embedetc=(
            discord.Embed(
                title="기타 명령어", 
                description="etc. Command",
                color=0xabcee9
            )
            .add_field(
                name=";서버",
                value="현재 서버컴퓨터 자원 사용량을 확인합니다"
            )
            .add_field(
                name=";ping",
                value="봇 레이턴시를 확인합니다."
            )
        )
        await ctx.send(
            embed=embedetc
        )
        
    @_help.command(name="학교", aliases=["school"])
    async def _helpschool(self, ctx):
        embedschool=(
            discord.Embed(
                title="학교관련 명령어", 
                description="school about Command",
                color=0xabcee9
            )
            .add_field(
                name=";급식",
                value="전국 학교 급식을 조회합니다"
            )
            .add_field(
                name=";시간표 < 학교 >",
                value="해당 학교를 시간표를 조회 합니다."
            )
        )
        await ctx.send(
            embed=embedschool
        )
        
        