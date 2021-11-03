import discord
import os
from tasks import TaskClass
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

### Jed's minecraft 1.18 prediction
date_pred = datetime(2021,11,26) # 11am


# init client
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    ### DO NOT MOVE - MUST ALWAYS BE ON TOP
    if message.author == client.user:
        return
    
    if message.content.startswith("$countdown"):
        date_now = datetime.now()
        x = date_pred - date_now
        minutes = (x.seconds//60)%60
        min_g = "{m} minutes".format(m=minutes)
        hours = x.seconds//3600
        hour_g = "{h} hours".format(h=hours)
        days = x.days
        day_g = "are {d} days".format(d=days)
        if (days == 1) : day_g = "is 1 day" #change grammar 
        if (hours == 1) : hour_g = "1 hour"
        if (minutes == 1) : min_g = "1 minute" 

        await message.channel.send("There {d}, {h}, {m} remaining until Jed's **Minecraft 1.18** release date prediction".format(d=day_g, h=hour_g, m=min_g))

client.run(TOKEN)
