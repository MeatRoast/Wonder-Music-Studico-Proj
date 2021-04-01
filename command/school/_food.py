import discord
from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import Bot
from discord.ext.commands import NoPrivateMessage
import traceback
import itertools
import requests
from bs4 import BeautifulSoup
import pandas
import asyncio
import urllib
import urllib.parse
import json
import time
import openpyxl


class _shfod(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(name='급식', aliases=['학교급식'])
    async def _shfod(self, ctx):
        embed=(
            discord.Embed(
                title="전국 초중고 급식 조회",
                description="오늘급식 뭐였지?",
                color=0x44d5bb
            )
            .add_field(
                name=";급식 조식 <학교이름>",
                value="해당 학교 조식을 조회합니다.",
                inline=False
            )
            .add_field(
                name=";급식 중식 <학교이름>",
                value="해당 학교 중식을 조회합니다.\n(대부분 급식 조회는 이걸로 하시면 됩니다.)",
                inline=False
            )
            .add_field(
                name=";급식 석식 <학교이름>",
                value="해당 학교 석식을 조회합니다.",
                inline=False
            )
        )
        if ctx.invoked_subcommand is None:
            await ctx.send(
                embed=embed
            )

    @_shfod.group(name="중식")
    async def _2food(self, ctx, arg1):

       database = openpyxl.load_workbook("schooldatabase.xlsx")





        #time1 = time.strftime('%Y%m%d')
        #sch2 = f'{arg1}'
        #key = "af99f8f3a3634b4ab56d67bd669a81ec"
        #surl = "https://open.neis.go.kr/hub/mealServiceDietInfo?"
        #test = f"ATPT_OFCDC_SC_CODE={koreaS_code}&SD_SCHUL_CODE={school_code}&MMEAL_SC_CODE=2&MLSV_YMD={time1}"
        #url = surl + test
        #response = requests.get(url)
        #soup = BeautifulSoup(response.text, "html.parser")
        #rlist = soup.findAll('row')
        #for r in rlist:
        #    sch = r.find('schul_nm')
        #    day = r.find('mlsv_ymd')
        #    dd = r.find('ddish_nm')
        #    테스트 = sch

        #print(f'{sch}')
        #print(f'{day}')
        #print(f'{dd}')
        #print(테스트)
        #embed2=(
        #    discord.Embed(
        #        title=f"1 급식 정보입니다",
        #        description="중식",
        #        color=0x44d5bb
        #    )
        #    .add_field(
        #        name=f"{dd}",
        #        value=f"{time1}",
        #        inline=Falses
        #    )
        #)
        #await ctx.send(
        #        embed=embed2
        #    )