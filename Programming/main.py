import discord
from discord.ext import commands
import os
import asyncio


token = open('token.txt')
TOKEN = token.read()


address = r"C:\Users\agent\Downloads\ffmpeg-4.3.2-2021-02-27-essentials_build\ffmpeg-4.3.2-2021-02-27-essentials_build\bin\ffmpeg.exe"


client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


    
    
@client.command(pass_content=True)
async def join (ctx):

  """:  Moves bot into your channel (only if you are in a channel)"""
  
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  
  if ctx.message.author.voice == None:
    await ctx.send("you must be in a voice chat first")
    return
  
  vc = ctx.message.author.voice.channel

  if voice and voice != None:
     await voice.move_to(vc)
  else:
    voice = await vc.connect()
  return
  
    
  
@client.command(pass_content=True)
async def sound (ctx,sample):
    
  """:  Plays the specified audio file"""

 
  s1 = "./samples/mp3-lion.mp3"
  s2 = ""
  s3 = ""

  guild = ctx.guild
  voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)

  #call !sound s1,2,3 etc replace sample
  audio_source = discord.FFmpegPCMAudio(sample)
  if voice_client != None:
    voice_client.play(audio_source, after=None)
    while voice_client.is_playing:
      await asyncio.sleep(.1)
      
  return    


@client.command(pass_content=True)
async def leave (ctx):

  """:  Makes bot leave voice channel"""
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  ##Check if its connected
  if voice!= None:
      await voice.disconnect()
  else:
      await ctx.send("the bot is not connected")

@client.command(pass_content=True)
async def check (ctx):
  print(ctx.author.voice)



client.run(TOKEN)