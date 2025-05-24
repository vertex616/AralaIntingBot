# AralaIntingBot

# Arala Inting Bot

Arala Inting Bot is a personal Discord bot that helps track and analyze League of Legends match performance for a specific player. The bot posts detailed match statistics to a Discord channel after each game, making it easy to review and discuss gameplay.

## Features

- Automatically fetches the latest League of Legends match for a specified summoner.
- Posts stats such as KDA, champion played, level, damage dealt, minions killed, time spent dead, and kill participation to a Discord channel.
- Designed for personal use and educational review.

## Requirements

- Python 3.8+
- [discord.py](https://pypi.org/project/discord.py/)
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

Install dependencies with:

```
pip install -r requirements.txt
```

## Setup

1. **Clone the repository** and navigate to the project folder.

2. **Create a `.env` file** in the project directory with your credentials:
    ```
    DISCORD_TOKEN=your-discord-bot-token
    RIOT_API_KEY=your-riot-api-key
    ```

3. **Edit `arsalan_history.py`** to set your summoner name, tag line, region, and Discord channel ID:
    ```python
    GAME_NAME = 'YourSummonerName'
    TAG_LINE = 'YourTagLine'
    REGION = 'your-region'
    CHANNEL_ID = your_discord_channel_id
    ```

4. **Run the bot:**
    ```
    python arsalan_history.py
    ```

## Notes

- **Never share your `.env` file or secrets publicly.**
- The bot is intended for personal, non-commercial use.
- The bot checks for new matches every hour (configurable in the code).

## License

This project is for personal use and educational purposes only.
