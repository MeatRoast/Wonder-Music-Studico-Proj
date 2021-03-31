from discord.ext import commands, tasks
from info import config
from itertools import cycle

status = cycle(
    [        
        '[ ;help ] 감사합니다!',
        'Copyright ©2021 Wonder-Music-Studico. All rights reserve"'
    ]
)


bot = commands.Bot(command_prefix=config['command_prefix'], description=config['description'])
