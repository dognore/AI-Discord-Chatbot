import discord 
from discord.ext import commands
import requests


bot = discord.ext.commands.Bot(command_prefix = '.',intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('บอทเริ่มการรับคําสั่ง')

@bot.command()
async def currency(ctx,type,curr):
  url = f"https://api.coingecko.com/api/v3/simple/price?ids={type}&vs_currencies={curr}"
  r = requests.get(url)
  data = r.json()
  await ctx.send(f'{type} มีมูลค่า {data[type][curr]} {curr}')

bot.run('ใส้tokenในนี้')
