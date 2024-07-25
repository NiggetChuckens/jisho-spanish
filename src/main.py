import os
from discord.ext import commands
from discord import Embed
from dotenv import load_dotenv
from jisho.jisho import jisho_traduction, get_jisho_sentence

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

#uses jisho website to get a word from japanese dictionary and translates to spanish
@bot.command(aliases=['jisho'])
async def jisho_dictionary(ctx, word):
    response = get_jisho_sentence(word)
    try:
        embed = Embed(
            title='Jisho Dictionary', 
            description='', 
            color=242424
        )
        for words in response:
            embed.description += f'Palabra: {words}\nTraduccion: {jisho_traduction(words)[1]}\n\n'
    
    except:
        response = jisho_traduction(word)
        embed = Embed(
            title='Jisho Dictionary', 
            description=f'Palabra: {word}\nTraduccion: {jisho_traduction(response)[1]}', 
            color=242424
        )

    await ctx.send(embed=embed)
    

bot.run(token)