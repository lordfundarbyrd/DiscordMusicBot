import discord
import os
import nacl

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

client = discord.Client()

token = open("token.txt","r") # token in .gitignore token.txt file
api_key = token.read()
token.close()

joined = False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("!join"):
        vc = await music_channel().connect()
        joined = True

    if msg.startswith("!leave"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                await vc.disconnect()
                joined = False

    #if msg.startswith("$inspire"):
        #quote = get_quote()
        #await message.channel.send(quote)

def music_channel():
    # TODO: make command for setting music channel
    music_id = 895154216887259157
    music_channel = client.get_channel(music_id)
    return music_channel

client.run(api_key)

