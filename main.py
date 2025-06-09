from dotenv import load_dotenv
import os
from discord_bot import AralaBot

load_dotenv()

def main():
    print("RIOT_API_KEY:", os.getenv('RIOT_API_KEY'))
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    # Read and parse multiple channel IDs
    CHANNEL_IDS = [int(cid.strip()) for cid in os.getenv('CHANNEL_IDS', '723635368192245870').split(',')]
    SUMMONER_NAME = os.getenv('GAME_NAME', 'ArsyQuan')

    intents = __import__('discord').Intents.default()
    bot = AralaBot(channel_ids=CHANNEL_IDS, summoner_name=SUMMONER_NAME, intents=intents)
    bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main()