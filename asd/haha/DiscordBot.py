'''
Created on 11.2.2021

@author: Jere Eskelinen
'''
# bot.py

import discord
import jsonToWorkWith

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '!ruokalista':
        jsonToWorkWith.resetLiha()
        jsonToWorkWith.liha()
        jsonToWorkWith.finishLiha()
        with open("ruokalistaLiha.txt", "r") as file:
            viesti = file.read()
        await message.channel.send(viesti)
        
    if message.content == '!kasvisruoka':
        jsonToWorkWith.resetKasvis()
        jsonToWorkWith.kasvis()
        jsonToWorkWith.finishKasvis()
        with open("ruokalistaKasvis.txt", "r") as file:
            viesti = file.read()
        await message.channel.send(viesti)
        
    if message.content == '!help':  
        await message.channel.send('Nykyiset komennot: !ruokalista, !kasvisruoka')
        
        
client.run('TOKEN')     
    