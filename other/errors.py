import logging
import discord
from discord.ext import commands

log = logging.getLogger('ErrorsCog')
log.setLevel('DEBUG')

class Errors(commands.Cog):
    """ Error handling """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.channel.send('Cannot use {} in private!'.format(ctx.command))
        elif isinstance(error, commands.CommandNotFound):
            return
        else:
            await ctx.channel.send('I broke! 😭 {}'.format(str(error)))
            # log these so we can catch them
            raise error

def setup(bot):
    cog = Errors(bot)
    bot.add_cog(cog)

def teardown(bot):
    bot.remove_cog('Errors')

