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

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("!user"):
        await message.channel.send(message.author)
        #print(message.author.voice.channel)

    if msg.startswith("!join"):
        if message.author.voice is None:
            await message.channel.send("Please join a channel, and then make me join")
        else:
            voice = discord.utils.get(client.voice_clients)

            if voice is None:
                destination = message.author.voice.channel
                vc = await destination.connect()
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

    #if msg.startswith("$inspire"):
        #quote = get_quote()
        #await message.channel.send(quote)

client.run(api_key)