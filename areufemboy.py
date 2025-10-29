import discord
from discord import app_commands
import random
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("Commands synced globally.")

client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.tree.command(name="femboy", description="Check femboy percentage")
@app_commands.describe(user="The user to check")
async def femboy(interaction: discord.Interaction, user: discord.User):
    percent = random.randint(0, 100)
    await interaction.response.send_message(f"{user.display_name} is {percent}% femboy!")

client.run(os.getenv('BOT_TOKEN'))
