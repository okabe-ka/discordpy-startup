import discord
from discord.ext import commands
import os
import traceback
import asyncio


token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 780094745640828998

client = discord.Client()

#bot = commands.Bot(command_prefix='/')



#async def input_number(num):
    #return num

#@client.command(aliases=['q'])
#@commands.dm_only() # DM以外でこのコマンドを入力するとエラーを吐く
@client.event
async def on_message(message):
    #frelist = []
    #mcount = int(message.content)
    #revmsg = text.format(mcount)

    #5桁での入力制限
    if not len(message.content) == 5:
        #await message.author.send('5桁で入力してください')
        return

    #DM以外に反応しない
    if message.guild !=  None:
        return

    #botからのメッセージに反応しない
    if message.author.bot:
        return

    #if not message.content.length == 5:
        #return

    if message.content.startswith(''):
        room_number = message.content



        #room_number = input('ルーム番号入力：')
        channel = client.get_channel(CHANNEL_ID)
        #room_number = message#
        msg = await channel.send('@everyone Scrim requested:'+str(room_number))
        [await msg.add_reaction(i) for i in ('⭕', '❌')]
        #await msg.add_reaction('⭕')

        #msg = await client.(message.channel, revmsg)
        ##if q == '⭕':
            #await number.channel.send(f'{number.author.mention} vs {number.author.mention} @ Room:' +str(number))
        #async def on_reaction_add(reaction , member ):
        def reaction_check(reaction,user):
            #guild = client.get_guild(member.guild.id)
            #channel = client.get_channel(reaction.message.channel.id)
            #are_same_messages = reaction.message.channel == msg.channel and reaction.message.id == msg.id
            return user == message.author#!= message.author.bot #and str(reaction.emoji) == '⭕'  and are_same_messages
            #return reaction.emoji


        #if target_reaction.emoji == '⭕':
            #await channel.send(room_number)
#,timeout=1800.0
#.exceptions
        count = 0
        while count <= 2:
            try:
                reaction, user = await client.wait_for('reaction_add',timeout=1000.0,check=reaction_check)
            except asyncio.exceptions.TimeoutError:
                await msg.delete()
                return
            else:
                if str(reaction.emoji) == '❌':
                    count+=1
                    if count >=1:
                        await msg.delete()
                        return
        #try:
            #reaction, user = await client.wait_for('reaction_add',timeout=900.0,check=reaction_check)
        #except asyncio.exceptions.TimeoutError:
        #    await msg.delete()
        #    return
        #else:
        #    if str(reaction.emoji) == '⭕':
                #count+=1
                #if count >=1:
        #        await channel.send(room_number)
        #        return


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

