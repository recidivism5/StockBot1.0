import discord
from pricegrabber import getEthPrice, getBtcPrice

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$eth'):
        await message.channel.send(getEthPrice())
    if message.content.startswith('$btc'):
        await message.channel.send(getBtcPrice())

    if message.content.startswith('$add'):
        try:
            s = message.content[4:].split()
            await message.channel.send(str(float(s[0]) + float(s[1])))
        except:
            await message.channel.send("Bruh")

client.run('PUT TOKEN HERE')
