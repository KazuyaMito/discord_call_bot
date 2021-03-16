import discord
from discord.ext import commands
import asyncio

class CallCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.voice = {}
        self.channel = {}

    @commands.command()
    async def call(self, ctx):
        vc = ctx.author.voice
        gid = ctx.guild.id

        if gid in self.voice:
            await self.voice[gid].disconnect()
            del self.voice[gid]
            del self.channel[gid]
        if not isinstance(vc, type(None)):
            self.channel[gid] = ctx.channel.id
            self.voice[gid] = await vc.channel.connect()
        else:
            await ctx.channel.send("まずはボイスチャンネルに入ってください")

        self.voice[gid].play(discord.FFmpegPCMAudio("call.mp3"))

        while True:
            if not self.voice[gid].is_playing():
                await self.voice[gid].disconnect()
                del self.voice[gid]
                del self.channel[gid]
                break

def setup(bot):
    bot.add_cog(CallCog(bot))