from dotenv import load_dotenv
import os
import discord
import asyncio
import requests

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
RIOT_API_KEY = os.getenv('RIOT_API_KEY')
GAME_NAME = 'ArsyQuan'
TAG_LINE = 'EUW'
REGION = 'euw1'  # Change to your friend's region
CHANNEL_ID = 723635368192245870  # Replace with your Discord channel ID
SUMMONER_NAME = GAME_NAME  # Define SUMMONER_NAME to avoid NameError

intents = discord.Intents.default()
client = discord.Client(intents=intents)

last_match_id = None

def get_puuid():
    url = f'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{GAME_NAME}/{TAG_LINE}'
    headers = {'X-Riot-Token': RIOT_API_KEY}
    response = requests.get(url, headers=headers)
    print("Account API response:", response.json())
    return response.json().get('puuid')

def get_latest_match_id(puuid):
    match_url = f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=1'
    headers = {'X-Riot-Token': RIOT_API_KEY}
    response = requests.get(match_url, headers=headers)
    matches = response.json()
    print("Match API response:", matches)  # Debug print
    if isinstance(matches, list) and matches:
        return matches[0]
    else:
        return None

def get_match_stats(puuid, match_id):
    match_url = f'https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}'
    headers = {'X-Riot-Token': RIOT_API_KEY}
    response = requests.get(match_url, headers=headers)
    match_data = response.json()
    print("Match details response:", match_data)  # Debug print

    player_team_id = None
    player_stats = None
    team_kills = 0

    # Find participant data for the given puuid and their team
    for participant in match_data.get('info', {}).get('participants', []):
        if participant['puuid'] == puuid:
            player_team_id = participant['teamId']
            player_stats = participant
            break

    if not player_stats:
        return None, None, None, None, None, None, None, None

    # Calculate team kills
    for participant in match_data.get('info', {}).get('participants', []):
        if participant['teamId'] == player_team_id:
            team_kills += participant['kills']

    k = player_stats['kills']
    d = player_stats['deaths']
    a = player_stats['assists']
    kda = f"{k}/{d}/{a}"
    score = player_stats.get('champLevel', 'N/A')
    damage = player_stats.get('totalDamageDealtToChampions', 'N/A')
    champ = player_stats.get('championName', 'Unknown')
    totalMinionsKilled = player_stats.get('totalMinionsKilled', 'N/A')
    victory = "Victory" if player_stats.get('win', False) else "Defeat"
    time_dead = player_stats.get('totalTimeSpentDead', 'N/A')

    # Calculate kill participation
    kill_participation = 0
    if team_kills > 0:
        kill_participation = round(((k + a) / team_kills) * 100, 1)
    else:
        kill_participation = 0

    return kda, score, damage, champ, totalMinionsKilled, victory, time_dead, kill_participation


async def check_for_new_match():
    global last_match_id
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    puuid = get_puuid()
    print("PUUID:", puuid)  # Debug print
    if not puuid:
        await channel.send(f"Could not find PUUID for {SUMMONER_NAME}. Check the summoner name and region.")
        return
    # In your check_for_new_match loop:
    while not client.is_closed():
        latest_match = get_latest_match_id(puuid)
        if latest_match and latest_match != last_match_id:
            last_match_id = latest_match
            kda, score, damage, champ, totalMinionsKilled, victory, time_dead, kill_participation = get_match_stats(puuid, latest_match)
            await channel.send(
                f"{SUMMONER_NAME} just finished a new match!\n"
                f"Result: {victory}\n"
                f"Champion: {champ}\n"
                f"KDA: {kda}\n"
                f"Level: {score}\n"
                f"Damage to Champions: {damage}\n"
                f"Total Minions Killed: {totalMinionsKilled}\n"
                f"Total Time Spent Dead: {time_dead} seconds\n"
                f"Kill Participation: {kill_participation}%"
            )
        await asyncio.sleep(500)  # Check every 1 hour

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(check_for_new_match())

client.run(DISCORD_TOKEN)