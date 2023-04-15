# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:40:29 2023

@author: BAUGER
"""

# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
#import nest_asyncio
#nest_asyncio.apply()
import discord
import os
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
# Define random drop
def random_dropres():
    import numpy, random
    tiles_available_res=("Why play it safe and boring when you can embrace the chaos and drop in the middle of the circle? It's like a box of chocolates, you never know what kind of surprise you're gonna get... probably a bullet to the face, but still! The middle it is.",    "Who needs cover when you have courage and stupidity? Dropping in the middle of the circle is like playing a game of Extreme Hide and Seek where everyone has a machine gun. The middle it is.",    "If you're not dropping in the middle of the circle, you're doing it wrong. Why spend half an hour looting and sneaking around when you can just jump into the meat grinder and pray for a miracle? The middle it is.",    "Dropping in the middle of the circle is the ultimate adrenaline rush. It's like a roller coaster, but instead of screaming and laughing, you're screaming and dying. The middle it is.",    "Forget about survival, dropping in the middle of the circle is like playing the lottery. You have a slim chance of winning, but if you do, you'll be the hero of the match... or the first one to die. Either way, it's a win-win situation! The middle it is.",    "Why bother with strategy when you can just drop in the middle of the circle and let the enemy do the thinking for you? The middle it is.",    "Dropping in the middle of the circle is like a baptism by fire. You'll either be reborn as a Warzone god or die trying. The middle it is.",    "Who needs a plan when you can just drop in the middle of the circle and hope for the best? It's like going to Vegas and putting all your chips on red. The middle it is.",    "Playing it safe is for amateurs. Dropping in the middle of the circle is for the elite few who have the guts and the lack of self-preservation. The middle it is.",    "The middle of the circle is like the heart of the Warzone. It's where all the action is, all the bloodshed, all the fun. The middle it is.",    "If you want to show off your skills and impress your teammates, dropping in the middle of the circle is the way to do it. Just make sure to have your last will and testament ready. The middle it is.",    "Dropping in the middle of the circle is like playing a game of Russian roulette, but instead of a gun, you have a parachute. The middle it is.",    "If you're not dropping in the middle of the circle, you're not living on the edge enough. Who needs a comfort zone when you can have a combat zone? The middle it is.",    "Dropping in the middle of the circle is the ultimate test of your survival skills. It's like being stranded in the wilderness with a bunch of heavily-armed psychopaths. The middle it is.",    "They say fortune favors the bold. Well, dropping in the middle of the circle is the boldest move you can make in Warzone. Just don't expect Lady Luck to stick around for too long. The middle it is.") 
    rand_tile = random.randint(0, (len(tiles_available_res)-1))
    return (tiles_available_res[rand_tile])
    del rand_tile
def random_drop():
    import numpy, random
    tiles_available = ('Passenger Train','Freight Train','B3','B4:Quarry','B5:Port','B6:Port','C2','C3','C4:Quarry','C5:Sattiq Cave Complex','C6','D2','D3:Rohan Oil','D4','D5:Sattiq Cave Complex','D6','D7:Cemetery','D8:Sawah Village','E2:Taraq Village','E3','E4:Zarqwa Hydro','E5','E6','E7','E8','F2:Al Mazrah City','F3:Al Mazrah City','F4','F5','F6:Ahkdar Village','F7:Sarrif Bay','F8:Fortress','G2:Al Mazrah City','G3:Al Mazrah City','G4:Marshland','G5:Al Sharim Pass','G6:Airport','G7:Airport','G8:Fortress','H4','H5','H6','H7:Airport','H8:Airport')    
    rand_tile = random.randint(0, (len(tiles_available)-1))
    return (("You are dropping {}!").format(tiles_available[rand_tile]))
    del rand_tile



# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
intents = discord.Intents.all()

bot = discord.Client(intents=intents)

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("Random Drop is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.

message_terms={'how large is pisters colon?':'It is the largest colon in all the land','who has the biggest dick of all the dicks?':'why, thats augs1515 of course.' }

@bot.event
async def on_message(message):
 	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".  
    if message.content in message_terms.keys():
        await message.channel.send(message_terms[message.content])      
    elif message.content =="/drop":
	# SENDS BACK A MESSAGE TO THE CHANNEL.
        await message.channel.send(random_drop())
    elif message.content =="/drop_res":
	# SENDS BACK A MESSAGE TO THE CHANNEL.
        await message.channel.send(random_dropres())        
    elif message.content == "/win":
        await message.channel.send("Fuck Yeah!, thats a dub!\n{}".format(r"https://tenor.com/view/will-ferrell-yes-win-winning-gif-23766394"))

     


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)
