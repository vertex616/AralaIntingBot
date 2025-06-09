import os
import discord
import asyncio
from riot_api import get_puuid, get_latest_match_id, get_match_stats

class AralaBot(discord.Client):
    def __init__(self, channel_ids, summoner_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel_ids = channel_ids
        self.summoner_name = summoner_name
        self.last_match_id = None

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        self.loop.create_task(self.check_for_new_match())

    async def check_for_new_match(self):
        await self.wait_until_ready()
        channels = [self.get_channel(cid) for cid in self.channel_ids]
        puuid = get_puuid()
        print("PUUID:", puuid)
        if not puuid:
            for channel in channels:
                if channel:
                    await channel.send(f"Could not find PUUID for {self.summoner_name}. Check the summoner name and region.")
            return
        while not self.is_closed():
            latest_match = get_latest_match_id(puuid)
            if latest_match and latest_match != self.last_match_id:
                self.last_match_id = latest_match
                kda, score, damage, champ, totalMinionsKilled, victory, time_dead, kill_participation, game_mode, lane = get_match_stats(puuid, latest_match)
                mention_user_id = os.getenv('MENTION_USER_ID')
                mention = f"<@{mention_user_id}>" if mention_user_id else self.summoner_name
                message = (
                    f"{mention} just finished a new match!\n"
                    f"Result: {victory}\n"
                    f"Game Mode: {game_mode}\n"
                    f"Lane: {lane}\n"
                    f"Champion: {champ}\n"
                    f"KDA: {kda}\n"
                    f"Level: {score}\n"
                    f"Damage to Champions: {damage}\n"
                    f"Total Minions Killed: {totalMinionsKilled}\n"
                    f"Total Time Spent Dead: {time_dead} seconds\n"
                    f"Kill Participation: {kill_participation}%"
                )
                for channel in channels:
                    if channel:
                        await channel.send(message)
            await asyncio.sleep(30)