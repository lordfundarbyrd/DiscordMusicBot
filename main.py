import discord
import os
import nacl

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

client = discord.Client()

api_key = '***'

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

    if msg.startswith("!leave"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                await vc.disconnect()

    #if msg.startswith("$inspire"):
        #quote = get_quote()
        #await message.channel.send(quote)

def music_channel():
    music_id = 895154216887259157
    music_channel = client.get_channel(music_id)
    return music_channel

client.run('ODk1MTE4NDE5NTg4OTQzODky.YVz5_Q.aYmYBrZfO8Z8KAIKvgXrGl3MCvg')

