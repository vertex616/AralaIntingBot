from dotenv import load_dotenv
import os
from discord_bot import AralaBot

load_dotenv()

def main():
    print("RIOT_API_KEY:", os.getenv('RIOT_API_KEY'))
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    CHANNEL_ID = int(os.getenv('CHANNEL_ID', 723635368192245870))
    SUMMONER_NAME = os.getenv('GAME_NAME', 'ArsyQuan')

    intents = __import__('discord').Intents.default()
    bot = AralaBot(channel_id=CHANNEL_ID, summoner_name=SUMMONER_NAME, intents=intents)
    bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main()