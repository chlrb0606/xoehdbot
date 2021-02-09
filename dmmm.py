import discord
from discord import Client
import os

client = discord.Client()


@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game("마크")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("너 곽태문")
    if message.content.startswith("갑철"):
        await message.channel.send("곽!갑!철")
    if message.content.startswith("민영"):
        await message.channel.send("고모 짱 이뻐")
    if message.content.startswith("태문"):
        await message.channel.send("왈왈 거북거북")
    if message.content.startswith("규헌"):
        await message.channel.send("존나 잘생김")
    if message.content.startswith("태령"):
        await message.channel.send("사촌형이 젤 이쁨")
    if message.content.startswith("태동"):
        await message.channel.send("나는 태:문이 사촌")
    if message.content.startswith("찬희"):
        await message.channel.send("태:문이가:롤 개못함")
    if message.content.startswith("건희"):
        await message.channel.send("다잉라이트 장인")
    if message.content.startswith("현준"):
        await message.channel.send("태:문아 너 편의점 가야됨")
    if message.content.startswith("재현"):
        await message.channel.send("재:현: 난 일찐 ㅋ")
    if message.content.startswith("수민"):
        await message.channel.send("가재맨 젖꼭지 빨고싶다")
    if message.content.startswith("준호"):
        await message.channel.send("fm하는데 나도 축구나 해볼까 ?")
    if message.content.startswith("승찬"):
        await message.channel.send("탈론 젖꼭지 빨아보고싶네")
    if message.content.startswith("젠지"):
        await message.channel.send("탈론 발가락 보고싶네")
    if message.content.startswith("이프"):
        await message.channel.send("나보다 못한년 ㅋ")

        
        
access_token = os.environ["BOT_TOKEN"]
client.run("ODA4MzU5NDMzMTc2MDg4NTc2.YCFZYw.RKq1ohV7GL3OaguBFEAa1qbd4AM")
