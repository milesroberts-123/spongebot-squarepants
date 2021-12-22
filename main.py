import discord
import os
import json
import random
import re
from os import listdir
from os.path import isfile, join

client = discord.Client()

def get_quote(character):
  f = open('spongebobQuotes.json',)
  json_data = json.load(f)
  json_data = json_data[character]
  json_len = len(json_data)
  j = random.randrange(json_len)
  quote = json_data[j]['q'] + " - " + character
  f.close()
  return(quote)

def get_conch():
  responses = ['Maybe someday.', 'Nothing.', 'Neither.', "I dont think so.", 'No.', 'Yes.', 'Try asking again.']
  return(responses[random.randrange(len(responses))])

def get_image():
  mypath = "./images"
  onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
  choice = random.randrange(len(onlyfiles))
  return(onlyfiles[choice])

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

### COMMANDS WITH RANDOM OUTPUTS ###
    if message.content.startswith('$quote'):
        words = message.content.split()
        if len(words) > 1:
            char = words[1]
            if char == "Spongebob":
                index = "Spongebob Squarepants"
            if char == "Patrick":
                index = "Patrick Star"
            if char == "Squidward":
                index = "Squidward Q. Tentacles"
            if char == "Sandy":
                index = "Sandra Jennifer Olivia 'Sandy' Cheeks"
            if char == "Krabs":
                index = "Eugene H. Krabs"
            if char == "Plankton":
                index = "Sheldon J. Plankton"
            if char == "Karen":
                index = "Karen Plankton"
            if char == "Gary":
                index = "Garold Wilson Jr. The Snail"
            if char == "Puff":
                index = "Mrs. Poppy Puff"
            quote = get_quote(index)
            await message.channel.send(quote)
        else:
            await message.channel.send("ERROR: Please specify a character to get a quote (Spongebob, Patrick, Squidward, Sandy, Krabs, Plankton, Karen, Puff, or Gary).")

    if message.content.startswith('$conch'):
        conch = get_conch()
        await message.channel.send(conch)

    if message.content.startswith('$image'):
       randomImage = get_image()
       await message.channel.send(file=discord.File("./images/" + randomImage))

### COMMANDS WITH NON-RANDOM OUTPUTS ###
# search the spongebob wiki
    if message.content.startswith('$search'):
       words = message.content.split()
       searchTerms = words[1:]
       searchString = "+".join(searchTerms)
       url = "https://spongebob.fandom.com/wiki/Special:Search?query=" + searchString + "&scope=internal&contentType=&ns%5B0%5D=0&ns%5B1%5D=114&ns%5B2%5D=115&ns%5B3%5D=500&ns%5B4%5D=502#"
       await message.channel.send(url)

client.run("ENTER TOKEN HERE BUT KEEP QUOTES")
