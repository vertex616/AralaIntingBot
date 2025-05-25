# AralaIntingBot

Arala Inting Bot is a personal Discord bot that tracks and analyzes League of Legends match performance for a specific player. The bot posts detailed match statistics to a Discord channel after each game, making it easy to review and discuss gameplay.

## Features

- Automatically fetches the latest League of Legends match for a specified summoner.
- Posts stats such as KDA, champion played, level, damage dealt, minions killed, time spent dead, and kill participation to a Discord channel.
- Modular code: Riot API logic and Discord bot logic are separated for maintainability.
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
   GAME_NAME=YourSummonerName
   TAG_LINE=YourTagLine
   REGION=your-region
   CHANNEL_ID=your_discord_channel_id
   ```

3. **Configure the bot:**

   - No need to edit code for credentials—just update your `.env` file.
   - Make sure your Discord bot is invited to your server and has permission to post in the target channel.

4. **Run the bot manually:**

   ```
   python main.py
   ```

5. **(Optional) Run the bot automatically at startup/logon:**
   - Use Windows Task Scheduler to run `main.py` with your virtual environment's Python interpreter.
   - Example XML for Task Scheduler is provided in project documentation or can be generated as needed.

## Notes

- **Never share your `.env` file or secrets publicly.**
- The bot is intended for personal, non-commercial use.
- The bot checks for new matches every 30 seconds (configurable in the code).

## Project Structure

```
AralaIntingBot/
├── main.py           # Entry point, loads env and starts the Discord bot
├── discord_bot.py    # Discord bot logic (AralaBot class)
├── riot_api.py       # Riot API functions
├── requirements.txt
├── .env
└── README.md
```

## License

This project is for personal use and educational purposes only.
