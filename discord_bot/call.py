import discord
from discord.ext import commands
import traceback
import ctypes

bot = commands.Bot(command_prefix='!')
token = ''
voice = {}
channel = {}

a = ctypes.util.find_library('opus')
b = discord.opus.load_opus(a)

@bot.command()
async def call(ctx):
    try:
        vc = ctx.author.voice
        gid = ctx.guild.id

        if gid in voice:
            await voice[gid].disconnect()
            del voice[gid]
            del channel[gid]
        if not isinstance(vc, type(None)):
            channel[gid] = ctx.channel.id
            voice[gid] = await vc.channel.connect()
        else:
            await ctx.channel.send("まずはボイスチャンネルに入ってください")
            return

        voice[gid].play(discord.FFmpegPCMAudio("call.mp3"))

        while True:
            if not voice[gid].is_playing():
                await voice[gid].disconnect()
                del voice[gid]
                del channel[gid]
                break
    except Exception:
        traceback.print_exc()

@bot.event
async def on_ready():
    print('---------')
    print(bot.user.name)
    print(bot.user.id)
    print('---------')

bot.run(token)