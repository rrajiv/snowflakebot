import discord
import asyncio
import logging

# read the token from the file
ftoken = open("token.txt", "r")

for line in ftoken:
    token = line

ftoken.close()

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event

# define the commands here to be supported
# !se <message> - send a msg to  all the people in the elite channel
# !sb <message> - send a msg to  all the people in the bunny channel
# !army <param> - adds your army manually
# !showarmy - shows a list of all armies
# !timer <reason> <time> - creates a timer for a <reason> for <time>
# !help - dump a list of commands by private msg

async def on_message(message):

    if (message.content.startswith('!help')):
        await client.send_message(message.author, "!se <message> - send a msg to  all the people in the elite channel")
        await client.send_message(message.author, "!sb <message> - send a msg to  all the people in the bunny channel")
        await client.send_message(message.author, "!army <param> - adds your army manually")
        await client.send_message(message.author, "!showarmy - shows a list of all armies")
        await client.send_message(message.author, "!timer <reason> <time> - creates a timer for a <reason> for <time>")
#        await client.send_message(message.author, "!help - dump a list of commands by private msg")

    if (message.content.startswith("!se") or message.content.startswith("!sb")):
        channels = client.get_all_channels()
        channelid = ""

        # go through each channel looking for "elitesnowflake" or "bunnysnowflake"
        for c in channels:
            if (message.content.startswith("!se") and c.name == "elitesnowflake"):
                print("channel name: " + c.name)
                print("channel id: " + c.id)
                channelid = c

            if (message.content.startswith("!sb") and c.name == "bunnysnowflake"):
                print("channel name: " + c.name)
                print("channel id: " + c.id)
                channelid = c


        # send a notify to everyone as long as the channel id is not empty
        # channel id will automatically define which channel to send
        # extract the message from the channel
        # if there is no message, send the default alert
        if (channelid != ""):
            inputmessage = str(message.content)
            channelmessage = inputmessage.split(" ", 1)

            if (len(channelmessage) > 1):
                await client.send_message(channelid, "@everyone - " + str(' '.join(channelmessage[1:])))
            else:
                await client.send_message(channelid, "@everyone - mass alert!")


    if (message.content.startswith("!army")):

        # get the channel of the message
        channelid = message.channel
        channelauthor = message.author

        # clean up the authorname by removing the hashes
        inputauthor = str(channelauthor).split("#",1)

        print("message sent by: " + str(inputauthor[0]) + " in " + str(channelid))

        # get the time
        inputattacktime = str(message.content)
        attacktime = inputattacktime.split(" ")

        print(attacktime)

        # can only accept 3 parameters - !army and <time> <reason>
        # multiply the value by seconds
        if (len(attacktime) == 3):
            calculatedattacktime = float(attacktime[1]) * 3600
            armyreason = attacktime[2]

            print("Sleeping for " + str(calculatedattacktime) + " because of " + str(armyreason))

            await asyncio.sleep(calculatedattacktime)
            await client.send_message(channelid, str(armyreason) + " is here - @" + str(inputauthor[0]))

client.run(token)