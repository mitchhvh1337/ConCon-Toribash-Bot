import discord
from discord.ext import commands
import requests
import datetime
import time
from itertools import cycle
import asyncio

token = "NDY4MTAxMTI3Nzc5NjQ3NDg4.Di0ovA.kVP8nI_RbOFqOSusspilxI-iaKg"
url = "http://forum.toribash.com/tori_stats.php?format=json&username="
client = commands.Bot("!")

@client.event
async def on_ready():
    print(discord.__version__)
    print("The bot is now ready to be used.")
    
@client.event
async def on_message(message):
    await client.process_commands(message)

@client.event
async def on_member_join(ctx, member):
    role = discord.utils.get(member.server.roles, name="Guest")
    await client.add_roles(member, role)

@client.command(pass_context = True)
async def stats(ctx):

    toriUsername = ctx.message.content[7:]

    if not toriUsername:
        await client.send_message(ctx.message.channel, "Please enter a username.")

    editedUrl = url + toriUsername  

    r = requests.get(editedUrl)

    print(editedUrl)

    tcToUsd = float(r.json()['tc'])
    tcToUsdO = tcToUsd / 18000
    tcToUsdOO = round(tcToUsdO, 2)

    print(str(tcToUsdOO))

    joinDate = datetime.datetime.fromtimestamp(int(r.json()['joindate'])).strftime('%d-%m-%Y %H:%M:%S')
    lastForumActivity = datetime.datetime.fromtimestamp(int(r.json()['lastactivity'])).strftime('%d-%m-%Y %H:%M:%S')
    lastIngameActivity = datetime.datetime.fromtimestamp(int(r.json()['lastingame'])).strftime('%d-%m-%Y %H:%M:%S')

    toriEmbed = discord.Embed(
        colour = discord.Colour.blue()
    )

    toriEmbed.set_footer(text = "Provided by Uke.")
    toriEmbed.set_thumbnail(url = "https://i.imgur.com/yPz7DQp.png")
    toriEmbed.add_field(name = "Username", value = r.json()['username'], inline = True)
    toriEmbed.add_field(name = "User ID", value = r.json()['userid'], inline = True)
    toriEmbed.add_field(name = "Belt", value = r.json()['belt'], inline = True)
    toriEmbed.add_field(name = "Belt Title", value = r.json()['belttitle'], inline = True)
    toriEmbed.add_field(name = "ELO", value = r.json()['elo'], inline = True)
    toriEmbed.add_field(name = "Win Ratio", value = r.json()['winratio'], inline = True)
    toriEmbed.add_field(name = "QI", value = r.json()['qi'], inline = True)
    toriEmbed.add_field(name = "TC", value = r.json()['tc'] + " ($" + str(tcToUsdOO) + ")", inline = True)
    toriEmbed.add_field(name = "Clan Name", value = r.json()['clanname'] + " (" + r.json()['clantag'] + ")", inline = False)
    toriEmbed.add_field(name = "Forum Posts", value = r.json()['posts'], inline = True)
    toriEmbed.add_field(name = "Joined Toribash", value = joinDate, inline = True)
    toriEmbed.add_field(name = "Last Forum Activity", value = lastForumActivity, inline = True)
    toriEmbed.add_field(name = "Last In-Game Activity", value = lastIngameActivity, inline = True)
    
    

    await client.send_message(ctx.message.channel, embed=toriEmbed)

@client.command(pass_context = True)
async def cmds(ctx):
    helpEmbed = (discord.Embed(description="Use .stats [Toribash Username] to get someone's toribash stats!"))
    helpEmbed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    helpEmbed.set_footer(text="Provided by ConBot")
    await client.send_message(ctx.message.channel, embed=helpEmbed)

@client.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    await client.kick(userName)
    await client.send_message(ctx.message.channel, "Kicked " + userName + " successfully.")

@client.command(pass_context = True)
async def conDab(ctx):
    await client.send_message(ctx.message.channel, "https://cdn.discordapp.com/attachments/461618928364552194/469218343438778385/unknown.png")

@client.command(pass_context = True)
async def conLove(ctx):
    await client.send_message(ctx.message.channel, "https://cdn.discordapp.com/attachments/461618928364552194/469219934702927882/unknown.png")

@client.command(pass_context = True)
async def conLick(ctx):
    await client.send_message(ctx.message.channel, "https://i.imgur.com/6Cwij6R.png")

@client.command(pass_context = True)
async def conHeyBaby(ctx):
    await client.send_message(ctx.message.channel, "https://image.prntscr.com/image/ofJirnjCQomckBUbeV6p_A.png")

client.run(token)