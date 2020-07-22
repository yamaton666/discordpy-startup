# -*- coding: utf-8 -*-
import discord

# コピーしたトークンをxxxに入れる
token = "Njk4NDc3ODA0MTUyNTUzNDky.Xxep5Q.M7R9IBkkVZZU_wGPtHMSoonpmAI"
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「やあ」というチャットが来た場合のメッセージ
    if message.content.startswith("いも"):
        # 送り主がチャットボット以外なら返事を返す
        if client.user != message.author:
            message = "いもです" + message.author.name
            await client.send_message(message.channel, message)

client.run(token)
