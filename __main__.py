# Import Library
from asyncio import run
from os import listdir

from discord import Intents
from discord.ext.commands import Bot, when_mentioned


# Import Value
from const import get_secret


# Start Code
intents = Intents()
intents.messages = True
intents.message_content = True
bot = Bot(when_mentioned, intents=intents)



@bot.event
async def on_ready():
    await bot.tree.sync()
    
    
async def load_extensions():
    for filename in listdir('cogs'):
        if not filename.endswith('.py'):
            continue
        
        cog_name = f'cogs.{filename[:-3]}'
        await bot.load_extension(cog_name)
        print(f'Cog loaded: {cog_name}')


def main():
    run(load_extensions())
    
    bot.run(get_secret('BOT_TOKEN'))
    
    
if __name__ == '__main__':
    main()