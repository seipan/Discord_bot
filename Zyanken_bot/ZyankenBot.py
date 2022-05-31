import asyncio
import re
import random, string
import discord
import time


TOKEN = "OTgxMTA3ODYxMDAwMTkyMDMw.GBcPBu.NO9hJ-PPg3tnBb_gQvrOcdzN0Y2lU-AizlQJQs"
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

    #受信したメッセージが"hey"だったとき"hello"を返す
    if message.content == '!zyanken':
        await message.channel.send('じゃんけんしようねー(gu:ぐー , pa:ぱー , tyoki:ちょき)')
        lst = []
        lst = ['gu','pa','tyoki']
        i = random.randint(0, 2)
        await message.channel.send('3秒後に出してね！！！(僕が出した後に出してね、、、)')
        await message.channel.send('3')
        time.sleep(1)
        await message.channel.send('2')
        time.sleep(1)
        await message.channel.send('1')
        await message.channel.send(lst[i])

        wait_message = await client.wait_for("message", check=check)

        if wait_message.content == 'gu':
            if lst[i] == 'gu':
                await message.channel.send('引き分け―')
            if lst[i] == 'tyoki':
                await message.channel.send('君の勝ち！！！')
            if lst[i] == 'pa':
                await message.channel.send('君の負け！！')

        if wait_message.content == 'tyoki':
            if lst[i] == 'gu':
                await message.channel.send('君の負け！！！')
            if lst[i] == 'tyoki':
                await message.channel.send('引き分け―')
            if lst[i] == 'pa':
                await message.channel.send('君の勝ち！！')

        if wait_message.content == 'pa':
            if lst[i] == 'gu':
                await message.channel.send('君の勝ち！！！')
            if lst[i] == 'tyoki':
                await message.channel.send('君の負け！！！')
            if lst[i] == 'pa':
                await message.channel.send('引き分けー')

client.run(TOKEN)