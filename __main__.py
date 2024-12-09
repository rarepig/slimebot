# Import Library
from discord import Intents
from discord.ext.commands import Bot, when_mentioned

# Import Value
import security

# Start Code
BOT_TOKEN = security.SLIMEBOT

intents = Intents()
bot = Bot(when_mentioned, intents=intents)


def main():
    bot.run(BOT_TOKEN)
    
    
if __name__ == '__main__':
    main()