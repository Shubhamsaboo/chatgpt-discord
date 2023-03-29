# main.py
import discord
from discord.ext import commands

from config import DISCORD_TOKEN
from chatgpt import generate_response

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command(name="ask")
async def ask(ctx, *, prompt):
    async with ctx.typing():
        response = await generate_response(prompt)
        await ctx.send(response)

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
