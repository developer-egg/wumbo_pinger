import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

EGG_ID = "not seeing my id today"
WOUBULBUS_ID = "not seeing his id today"

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.id == EGG_ID:
        if "@everyone" in message.content or "@.everyone" in message.content:
            await message.channel.send(f"<@{WOUBULBUS_ID}> Something might be important")

client.run("not stealing my token today")
