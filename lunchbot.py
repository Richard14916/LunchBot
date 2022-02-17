import os
from dotenv import load_dotenv
import discord 
from discord.ext import commands
from datetime import datetime
import pytz

tz_caltech = pytz.timezone('US/Pacific')

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

def check_lunch_time():
    pc_time_rn = datetime.now(tz_caltech)
    hour = pc_time_rn.hour
    minute = pc_time_rn.minute
    if 60 * hour + minute > 660 and 60 * hour + minute < 930:
        return True
    else:
        return False

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='lunchtime', help="Is it lunch yet?")
async def respond_lunchtime(ctx):
    if ctx.message.channel.name == 'lunch':
        if check_lunch_time():
            is_it_lunch = "It's lunchtime!"
        else:
            is_it_lunch = "It's not time for lunch yet :("
        await ctx.send(is_it_lunch)
    else:
        return

@bot.command(name="clowns_assemble", help="Summon the clowns for lunch - pass a time to declare assembly time")
async def summon_clowns(ctx, assembly_time=None):
    if assembly_time is None:
        assembly_time = datetime.now(tz_caltech).strftime("%H:%M")
    if ctx.message.channel.name == 'lunch':
        if check_lunch_time():
            clown = discord.utils.get(ctx.guild.roles, name="🤡")
            summons_message = "{} you are summoned for lunch at {}, clowns.".format(clown.mention, assembly_time)
        else:
            summons_message = "You can't summon the clowns, it's not lunch time yet!"
        await ctx.send(summons_message)
    else:
        return


bot.run(TOKEN)