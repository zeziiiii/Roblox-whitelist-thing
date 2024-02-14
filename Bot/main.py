import nextcord
from nextcord.ext import commands
import random
import string
import base64
import httpx

bot = commands.Bot()

def lol(key):
    encoded_base64 = base64.b64encode(key.encode()).decode()
    encoded_base64 = encoded_base64.rstrip('=')
    return encoded_base64

async def kys(key):
    url = 'https://example.com/'
    params = {'key': key}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
    return response.text

@bot.slash_command(description="Generate and send a random key to a user")
async def key(interaction: nextcord.Interaction, user: nextcord.User):
    wow = ''.join(random.choices(string.ascii_letters + string.digits, k=15))
    key = lol(wow)
    await kys(key)
    await user.send(embed=nextcord.Embed(title="Generated Key", description=f"Here is your key: {key}", color=0x3498db))
    await interaction.response.send_message(f"Sent to {user}", ephemeral=True)

bot.run('botoken')
