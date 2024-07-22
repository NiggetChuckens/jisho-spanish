import os
from discord.ext import commands
from discord import Embed
from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import load_dotenv
from jisho.jisho import jisho_traduction

load_dotenv()
token = os.getenv('YUKI-TEST')  
bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
#purge 'x' amount of messages
@bot.command(aliases= ["purge","delete"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=None):
    if amount is None:
        await ctx.channel.purge(limit=2)
    else:
        await ctx.channel.purge(limit=int(amount))

#uses jisho website to get a word from japanese dictionary and translates it into spanish
@bot.command(aliases=['jisho'])
async def jisho_dictionary(ctx, word):
    embed = Embed(title='Jisho Dictionary', description=f'Palabra: {word}\nTraduccion: {jisho_traduction(word)[1]}', color=242424)
    await ctx.send(embed=embed)
    

bot.run(token)