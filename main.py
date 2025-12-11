import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"You have logged in as {bot.user}")

    channel = bot.get_channel() #masukan server id
    if channel is not None:
        await channel.send("Halo saya adalah Environmental_bot, saya akan memberikan bantuan cara mengurangi sampah di rumah anda. \n berikut command yang anda bisa pakai: \n $commands \n $tips")
    else:
        print("Channel not found!")

@bot.command()
async def commands(ctx):
    await ctx.send(f'List perintah: \n $commands \n tips')
    
@bot.command()
async def tips(ctx):
    choice=random.randint(1,3)
    if choice == 1:
        await ctx.send(file=discord.File("Images/Meme1.jpg"))
        await ctx.send(f'Hindari Produk Sekali Pakai: Bawa tas belanja, botol minum, dan wadah makan sendiri saat bepergian.')
    elif choice == 2:
        await ctx.send(file=discord.File("Images/Meme2.jpg"))
        await ctx.send(f'Belanja Cerdas: Beli secukupnya sesuai kebutuhan agar tidak ada makanan atau barang yang terbuang.')
    elif choice == 3:
        await ctx.send(file=discord.File("Images/Meme3.jpg"))
        await ctx.send(f'Manfaatkan Wadah: Gunakan kembali botol plastik atau wadah bekas untuk menanam tanaman atau kebutuhan lain.')
    else:
        await ctx.send("error")


bot.run("")

