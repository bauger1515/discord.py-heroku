# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
#import nest_asyncio
#nest_asyncio.apply()
import discord
import os
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
# Define random drop
def random_drop():
    import numpy, random
    tiles_available = ('B3','B4:Quarry','B5:Port','B6:Port','C2','C3','C4:Quarry','C5:Sattiq Cave Complex','C6','D2','D3:Rohan Oil','D4','D5:Sattiq Cave Complex','D6','D7:Cemetery','D8:Sawah Village','E2:Taraq Village','E3','E4:Zarqwa Hydro','E5','E6','E7','E8','F2:Al Mazrah City','F3:Al Mazrah City','F4','F5','F6:Ahkdar Village','F7:Sarrif Bay','F8:Fortress','G2:Al Mazrah City','G3:Al Mazrah City','G4:Marshland','G5:Al Sharim Pass','G6:Airport','G7:Airport','G8:Fortress','H4','H5','H6','H7:Airport','H8:Airport')    
    rand_tile = random.randint(0, (len(tiles_available)-1))
    return (("You are dropping:{}!").format(tiles_available[rand_tile]))

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
    elif message.content == "/win":
	await message.channel.send(("Fuck Yeah!, Dubs for everyone! {}").format("https://tenor.com/view/will-ferrell-yes-win-winning-gif-23766394"))

	
        
https://tenor.com/view/will-ferrell-yes-win-winning-gif-23766394

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)
