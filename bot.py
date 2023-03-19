import discord
import os
from dotenv import load_dotenv
load_dotenv()

# Prompt the user for their token
TOKEN = os.environ['TOKEN']

# Create a client instance
intents = discord.Intents.all()

client = discord.Client(intents=intents)

# Prompt the user for the channel ID
@client.event
async def on_ready():
    channel_id = input("Enter the channel ID: ")
    channel = client.get_channel(int(channel_id))
    if channel is None:
        print("Invalid channel ID!")
    else:
        await channel.send("Hello, world!")

def run_discord_bot():
    intents = discord.Intents.all()

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print('Logged in as {0.user}'.format(client))

    @client.event
    async def on_raw_reaction_add(payload):
        if payload.emoji.name == '👋' and payload.member.bot == False:
            channel = await client.fetch_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            if len([r for r in message.reactions if str(r) == '👋']) >= 1:
                destination_channel_id = 956905099496677447
                destination_channel = await client.fetch_channel(destination_channel_id)
                await destination_channel.send(f"{message.author.mention} posted a hall of fame message: {message.content}")
                #If the message body is empty, copy the image or embed
                if message.content == "":
                    if message.attachments:
                        await destination_channel.send(message.attachments[0].url)
                    #If audio, embed the audio
                    elif message.audio:
                        await destination_channel.send(message.audio)
                    else:
                        #Copy Message to the hall of fame channel
                        await destination_channel.send(message.content)
                
                


    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)
