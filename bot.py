import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

load_dotenv()


TOKEN = str(os.getenv("TOKEN"))

images = os.path.join('ManulMemes\\ShinyMemes\\media', 'images')



client = discord.Client()

bot = commands.Bot(command_prefix='!')


@bot.command(name='meme', help='Memes.')
async def send_image(ctx):
    images = os.path.join('ManulMemes\\ShinyMemes\\media', 'images')
    filenames = os.listdir(images)
    selected_file = os.path.join(images, random.choice(filenames))
    await ctx.send(file=discord.File(selected_file))

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


bot.run(TOKEN)
client.run(TOKEN)