import nextcord
from nextcord.ext import commands
import random
import string
import base64
import httpx

bot = commands.Bot()


def remove(user_id):
    with open('keys.txt', 'r') as f:
        lines = f.readlines()
    with open('keys.txt', 'w') as f:
        for line in lines:
            if not line.split('=')[0].endswith(str(user_id)):
                f.write(line)
async def kys(key):
    url = 'https://example.com/'
    params = {'key': key}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
    return response.text

async def kyss(key):
    url = 'https://example.com/'
    params = {'keydelete': key}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
    return response.text

@bot.slash_command(description="Generate and send a random key to a user")
async def key(interaction: nextcord.Interaction, user: nextcord.User):
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=15))
    await kys(key)
    with open('keys.txt', 'a') as f:
        f.write(f"{user.name}/{user.id}={key}\n")
    await user.send(embed=nextcord.Embed(title="Generated Key", description=f"Here is your key: {key}", color=0x3498db))
    await interaction.response.send_message(f"Sent to {user}", ephemeral=True)


@bot.slash_command(description="Delete a key for a specific user")
async def deletekey(interaction: nextcord.Interaction, user: nextcord.User):
    with open('keys.txt', 'r') as f:
        lines = f.readlines()
    bye = None
    for line in lines:
        if line.split('=')[0].endswith(str(user.id)):
            bye = line.split('=')[1].strip()
            break
    if bye:
        await kyss(bye)
        remove(user.id)
        embed = nextcord.Embed(title="Key Deleted", description=f"The key **{bye}** that was affiliated with the user **{user.name}/{user.id}** has been deleted.", color=0x3498db)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        await interaction.response.send_message("Key not found for the specified user.", ephemeral=True)

print("Working")
bot.run('token')
