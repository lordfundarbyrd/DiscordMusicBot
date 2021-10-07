import discord
import os
import nacl

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

client = discord.Client()
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

token = open("token.txt","r") # tokens in .gitignore token.txt file
d_api_key = token.readline()
yt_api_key = token.readline()
token.close()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    # prints the username of the user who used the !user command
    if msg.startswith("!user"):
        await message.channel.send(message.author)
        #print(message.author.voice.channel)

    # makes bot join channel user is currently in
    #TODO: add command for setting default channel (right now message is just sent)
    if msg.startswith("!join"):
        if message.author.voice is None:
            await message.channel.send("Please join a channel, and then make me join")
        else:
            voice = discord.utils.get(client.voice_clients)

            #joins channel if not already in channel
            if voice is None:
                destination = message.author.voice.channel
                vc = await destination.connect()
            # disconnects from current channel and joins new channel
            else:
                for vc in client.voice_clients:
                    if vc.guild == message.guild:
                        await vc.disconnect()
                destination = message.author.voice.channel
                vc = await destination.connect()

    if msg.startswith("!leave"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                await vc.disconnect()

    if msg.startswith("!yt"):
        #print(msg[4:])
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secrets.json"

        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
        credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id="Ks-_Mh1QhMc"
        )

        response = request.execute()

        print(response)

    #if msg.startswith("$inspire"):
        #quote = get_quote()
        #await message.channel.send(quote)

client.run(d_api_key)