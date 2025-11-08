import os
import discord
from discord import app_commands
from discord.ext import commands

# Intents are required for Discord API v2
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Synced {len(synced)} slash commands")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")

# @bot.command()
# async def hello(ctx):
#     await ctx.send("Hello there! 👋")

# Example slash command
@bot.tree.command(name="hello", description="Say hello to the bot!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"👋 Hello {interaction.user.name}!")


# Run your bot
bot.run("RlBqCxyhM1kGCxQU0ivp31F-qCipNnYi")
# bot.run(os.getenv('TOKEN'))






