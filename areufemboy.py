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
        for guild in self.guilds:
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
        print(f"Synced to {len(self.guilds)} servers")

    async def on_guild_join(self, guild):
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)
        print(f"Synced to new server: {guild.name}")

client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f'Bot ONLINE: {client.user}')

@client.tree.command(name="femboy", description="Check femboy percentage")
@app_commands.describe(user="The user to check")
async def femboy(interaction: discord.Interaction, user: discord.User):
    percent = random.randint(0, 100)
    await interaction.response.send_message(f"{user.display_name} is **{percent}%** femboy! 🏳️‍⚧️")

@client.tree.command(name="setfemboy", description="Set femboy percentage manually")
@app_commands.describe(user="The user to check", percent="The femboy percentage (0-100)")
async def set_femboy(interaction: discord.Interaction, user: discord.User, percent: int):
    if 0 <= percent <= 100:
        await interaction.response.send_message(f"{user.display_name} is **{percent}%** femboy! 🏳️‍⚧️")
    else:
        await interaction.response.send_message("Please enter a valid percentage between **0** and **100**.")

client.run(os.getenv('BOT_TOKEN'))
