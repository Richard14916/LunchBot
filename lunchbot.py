import os
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime
import pytz

tz_caltech = pytz.timezone('US/Pacific')

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='lunch', help="Is it lunch yet?")
async def check_lunch(ctx):
    if ctx.message.channel.name == 'lunch':
        pc_time_rn = datetime.now(tz_caltech)
        hour = pc_time_rn.hour
        minute = pc_time_rn.minute
        if 60 * hour + minute > 660 and 60 * hour + minute < 930:
            is_it_lunch = "It's lunchtime!"
        else:
            is_it_lunch = "It's not time for lunch yet :("
        await ctx.send(is_it_lunch)
    else:
        return


bot.run(TOKEN)