import discord
from bot_logic import *
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print("Se inicio el bot")

@bot.command()
async def hola(ctx):
    await ctx.send("Hola, como estas")

@bot.command()
async def suma(ctx,num1:int,num2:int):
    suma = num1 + num2
    await ctx.send(f'La suma de {num1} + {num2} = {suma}')

@bot.command()
async def password(ctx, num:int):
    password = gen_pass(num)
    await ctx.send(password)

@bot.command()
async def coin(ctx):
    coin_side = flip_coin()
    await ctx.send(coin_side)

@bot.command()
async def meme(ctx): 
    imagen = random.choice(os.listdir('images'))
    with open(f'images/{imagen}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def fox(ctx):
    image_url = get_fox_image_url()
    await ctx.send(image_url)

bot.run("Token")
