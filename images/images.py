from discord.ext import commands


class Images:
    def __init__(self, bot):
        self.bot = bot
        self.base = 'data/images/'

    @commands.command(pass_context=True)
    async def dj(self, context):
        """Shows information on becoming a DJ"""
        await self.bot.send_file(context.message.channel, '{}dj.png'.format(self.base))

def setup(bot):
    n = Images(bot)
    bot.add_cog(n)
