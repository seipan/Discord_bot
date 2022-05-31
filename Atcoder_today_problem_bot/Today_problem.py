import asyncio
import re
import random, string
import discord
import time


TOKEN = "OTgxMTU0NTE2Nzg5NTE0MjYw.GqNnJ0.IGou7xAeChuSxkKMkxWq6un3T7CcFkUzniyCxg"
client = discord.Client()

#bot起動完了時に実行される処理
@client.event
async def on_ready():
    print('ログイン成功')

#メッセージ受信時に実行される処理
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    def check(msg):
        return msg.author == message.author

    if message.content == '!Atcoder':
        await message.channel.send('ABC?ARC?AGC?')
        wait_message = await client.wait_for("message", check=check)

        if wait_message.content == 'ABC':
            i = random.randint(1, 253)
            s = "https://atcoder.jp/contests/abc"
            i_str = str(i)
            while len(i_str)<3:
                i_str = '0'+i_str
            s = s+i_str
            s = s+"/tasks/"
            s = s+"abc"+i_str+'_'

            await message.channel.send('今回はABC'+i_str+'です。何問題ですか?(ex. a)(小文字で)')
            wait_message2 = await client.wait_for("message", check=check)

            s = s + wait_message2.content
            await message.channel.send(s)

        if wait_message.content == 'ARC':
            i = random.randint(1, 141)
            s = "https://atcoder.jp/contests/arc"
            i_str = str(i)
            while len(i_str)<3:
                i_str = '0'+i_str
            s = s+i_str
            s = s+"/tasks/"
            s = s+"arc"+i_str+'_'

            await message.channel.send('今回はARC'+i_str+'です。何問題ですか?(ex. a)(小文字で)')
            wait_message2 = await client.wait_for("message", check=check)

            s = s + wait_message2.content
            await message.channel.send(s)

        if wait_message.content == 'AGC':
            i = random.randint(1, 57)
            s = "https://atcoder.jp/contests/agc"
            i_str = str(i)
            while len(i_str)<3:
                i_str = '0'+i_str
            s = s+i_str
            s = s+"/tasks/"
            s = s+"agc"+i_str+'_'

            await message.channel.send('今回はAGC'+i_str+'です。何問題ですか?(ex. a)(小文字で)')
            wait_message2 = await client.wait_for("message", check=check)

            s = s + wait_message2.content
            await message.channel.send(s)







client.run(TOKEN)