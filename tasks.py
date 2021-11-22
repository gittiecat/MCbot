from discord.ext import tasks, commands
from datetime import datetime, timedelta

class TaskClass(commands.Cog):
    def __init__(self,client):
        self.next = datetime.now()+timedelta(days=1)
        self.next = self.next.replace(hour=7, minute=0, second=0, microsecond=0)
        self.client = client
        self.morning.start()

    def cog_unload(self):
        self.morning.cancel()

    @tasks.loop(seconds=1.0)
    async def morning(self):
        try:
            print(len(self.client.guilds[1].get_member(480755393891663874)))
            print("---")
        except:
            print("whoopsie")

        if (self.next < datetime.now()):
            self.next = datetime.now()+timedelta(days=1)
            self.next = self.next.replace(hour=7, minute=0, second=0, microsecond=0)