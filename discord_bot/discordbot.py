import discord
from discord.ext import commands
import ctypes
import ctypes.util
import traceback

INITIAL_EXTENSIONS = [
    'cogs.testcog'
]

class MyBot(commands.Bot):
    
    def __init__(self, command_prefix):
        
        super().__init__(command_prefix)
        
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

        a = ctypes.util.find_library('opus')
        b = discord.opus.load_opus(a)

    async def on_ready(self):
        print('---------')
        print(self.user.name)
        print(self.user.id)
        print('---------')


if __name__ == '__main__':
    bot = MyBot(command_prefix='!')
    bot.run('ODIwOTk1Mjc3NTExMDY1NjUw.YE9Rbw.AfAX3MuSfitieW0I0cySqfdGu_s')