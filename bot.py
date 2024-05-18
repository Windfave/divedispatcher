import discord
from discord import app_commands
from discord.ext import commands
import requests
import datetime

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all(),status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="orders"))



@bot.event
async def on_ready():
    print('Bot is online.')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
        
    except Exception as e:
        print(e)

@bot.tree.command(name="planetinfo", description="This commands shows all active planets we are fighting for and their status and description.")
async def PlanetInfo(interaction: discord.Interaction):
    response = requests.get("https://helldiverstrainingmanual.com/api/v1/war/campaign")
    if response.status_code == 200:
        data = response.json()
        embeds = []
        for planet in data:
            color = get_color(int(planet['percentage']))

            embed = discord.Embed(
                title=planet["name"],
                color=color
            )
            embed.add_field(name="Faction", value=planet["faction"], inline=False)
            embed.add_field(name="Players", value=planet["players"], inline=False)
            embed.add_field(name="Health", value=f"{planet['health']}/{planet['maxHealth']}", inline=False)
            embed.add_field(name="Percentage", value=f"{planet['percentage']}%", inline=False)
            
            # Check if biome information is available
            if planet["biome"] is not None:
                embed.add_field(name="Biome", value=planet["biome"]["description"], inline=False)
            else:
                embed.add_field(name="Biome", value="No biome information available", inline=False)
            
            embeds.append(embed)

        if embeds:
            total_planets = len(data)
            total_embed = discord.Embed(
                title="Total Active Planets being fought:",
                color=discord.Color.green() 
            )
            total_embed.add_field(name="Total Planets", value=total_planets, inline=False)
            await interaction.response.send_message(embed=embeds[0])  # Sending the first embed
            
            for embed in embeds[1:]:  # Sending subsequent embeds in separate messages
                await interaction.followup.send(embed=embed)
                
            await interaction.followup.send(embed=total_embed)  # Sending total planets info
        else:
            await interaction.response.send_message("No data available.")
    else:
        await interaction.response.send_message("Failed to fetch data from the API")
        
def get_color(percentage):
    if percentage > 55:
        return discord.Color.brand_green()
    elif 45 <= percentage <= 55:
        return discord.Color.default()
    else:
        return discord.Color.brand_red()

@bot.tree.command(name="news", description="This commands shows 10 latest news from the ingame news feed from the HD2 API.")
async def News(interaction: discord.Interaction):
    response = requests.get("https://helldiverstrainingmanual.com/api/v1/war/news")
    if response.status_code == 200:
        data = response.json()
        embeds = []
        for news_item in data:
            embed = discord.Embed(
                title=f"News ID: {news_item['id']}",
                description=news_item['message'],
                color=discord.Color.green()
            )
            embeds.append(embed)

        if embeds:
            await interaction.response.send_message(embeds=embeds)
        else:
            await interaction.response.send_message("No news available.")
    else:
        await interaction.response.send_message("Failed to fetch news from the API")

def convert_timestamp(timestamp):
    try:
        # Convert the timestamp to datetime object
        return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        # Print any errors that occur during conversion
        print(f"Error converting timestamp: {e}")
        return "Invalid Timestamp"



bot.run("token")
