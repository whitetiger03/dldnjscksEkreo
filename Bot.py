import discord
import datetime
import os
import time
import pytz
import asyncio
from discord.ext import tasks
from itertools import cycle

client = discord.Client()

@client.event
async def on_ready():
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드 봇 이름 : " +client.user.name)
    print("디스코드 봇 ID" +str(client.user.id))
    print("디스코드봇 버전 : " + str(discord.__version__))
    print('------')
    
    change_status.start()
    
status = cycle(["Visual Studio Code", "Dev C++", "!도움말", "ZOOM"])
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_message(message):
    content = message.content

    if content.startswith("!자기소개"):
        embed=discord.Embed(description="응애 나는 IT소프트웨어과 과디코 도우미 봇", color=0x00ff56)
        embed.set_author(name="응애 나 아기 디코봇")
        await message.channel.send(embed=embed)

    if content.startswith("!시간표"):
        embed=discord.Embed(title=" ", description=" ", color=0x00ff56)
        embed.set_author(name="```수원정보과학고등학교 1학년 9반 시간표```", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)

    if content.startswith("!월시간표"):
        embed=discord.Embed(description="<1교시>\n프로\n임미경선생님\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n\n<2교시>\n프로\n임미경선생님\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n\n<3교시>\n프로\n임미경선생님\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n\n<4교시>\n프로\n임미경선생님\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n\n<5교시>\n수학\nhttps://us02web.zoom.us/j/7076631677?pwd=RkVPYzRXcDVrdXM3VEUyTlBHMXN2Zz09\n\n<6교시>\n사회\n이용각선생님\nhttps://us02web.zoom.us/j/9546996730\n암호 : 810052", color=0x00ff56)
        embed.set_author(name="IT 소프트웨어과 1-9 월요일 시간표", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)
    
    if content.startswith("!화시간표"):
        embed=discord.Embed(description="<1교시>\n체육\nhttps://us02web.zoom.us/j/5523718127?pwd=TEhQeFJaanJ0dVVuOUVIdzFJUTRIUT09\n암호 : 2246\n\n<2교시>\n컴일\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n\n<3교시>\n컴일\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n\n<4교시>\n영어\nhttps://zoom.us/j/7334811715?pwd=TnAwc2dMeWFHYlRWdkFocTlQVWVlQT09\n\n<5교시>\n수학\nhttps://us02web.zoom.us/j/7076631677?pwd=RkVPYzRXcDVrdXM3VEUyTlBHMXN2Zz09\n\n<6교시>\n음악\nhttps://zoom.us/j/3079582246?pwd=clh3Ym82NGNDZXZlTC9yUzR2RUhnZz09\n암호 : 2246\n\n<7교시>\n사회\n이진경선생님\nhttps://zoom.us/j/9785974688\n암호 : 4688", color=0x00ff56)
        embed.set_author(name="IT 소프트웨어과 1-9 화요일 시간표", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)

    if content.startswith("!수시간표"):
        embed=discord.Embed(description="<1교시>\n국어\nhttps://us02web.zoom.us/j/8980834250\n암호 : 4250\n\n<2교시>\n음악\nhttps://zoom.us/j/3079582246?pwd=clh3Ym82NGNDZXZlTC9yUzR2RUhnZz09\n암호 : 2246\n\n<3교시>\n수학\nhttps://us02web.zoom.us/j/7076631677?pwd=RkVPYzRXcDVrdXM3VEUyTlBHMXN2Zz09\n\n<4교시>\n영어\nhttps://zoom.us/j/7334811715?pwd=TnAwc2dMeWFHYlRWdkFocTlQVWVlQT09\n\n<5교시>\n사회\n이용각선생님\n\nhttps://us02web.zoom.us/j/9546996730\n암호 : 810052\n\n<6교시>\n과학\nhttps://zoom.us/j/8212455526?pwd=SnRkaFBZU05ETHFWOExRMXJlc243Zz09\n암호 : 5526\n\n<7교시>\n진로\nhttps://us02web.zoom.us/j/7414780713?pwd=aDdiYldHVTRScVk3WjFQMG9SQkxUQT09\n암호 : 1234", color=0x00ff56)
        embed.set_author(name="IT 소프트웨어과 1-9 수요일 시간표", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)

    if content.startswith("!목시간표"):
        embed=discord.Embed(description="<1교시>\n과학\nhttps://zoom.us/j/8212455526?pwd=SnRkaFBZU05ETHFWOExRMXJlc243Zz09\n암호 : 5526\n\n<2교시>\n프로\n박진영선생님\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n\n<3교시>\n프로\n박진영선생님\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n\n<4교시>\n체육\nhttps://us02web.zoom.us/j/5523718127?pwd=TEhQeFJaanJ0dVVuOUVIdzFJUTRIUT09\n암호 : 2246\n\n<5교시>\n국어\nhttps://us02web.zoom.us/j/8980834250\n암호 : 4250\n\n<6교시>\n영어\nhttps://zoom.us/j/7334811715?pwd=TnAwc2dMeWFHYlRWdkFocTlQVWVlQT09\n\n<7교시>\n사회\n이진경선생님\nhttps://zoom.us/j/9785974688\n암호 : 4688", color=0x00ff56)
        embed.set_author(name="IT 소프트웨어과 1-9 목요일 시간표", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)

    if content.startswith("!금시간표"):
        embed=discord.Embed(description="<1교시>\n미술\n\n<2교시>\n미술\n\n<3교시>\n처리\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n\n<4교시>\n처리\nhttps://zoom.us/j/3477694372?pwd=NlIvbDlGRHVKQlQ4WVphSVg3RkJOQT09#success\n\n<5교시>\n융합\nhttps://us02web.zoom.us/j/7076631677?pwd=RkVPYzRXcDVrdXM3VEUyTlBHMXN2Zz09\n\n<6교시>\n창체\nhttps://us02web.zoom.us/j/7076631677?pwd=RkVPYzRXcDVrdXM3VEUyTlBHMXN2Zz09\n", color=0x00ff56)
        embed.set_author(name="IT 소프트웨어과 1-9 금요일 시간표", url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/873384182997479457/879342240839905360/unknown.png")
        await message.channel.send(embed=embed)

    if content.startswith("!시정표"):
        embed=discord.Embed(description="<1교시>\n09:10 ~ 10:00\n\n<2교시>\n10:10 ~ 11:00\n\n<3교시>\n11:10 ~ 12:00\n\n<4교시>\n12:10 ~ 1:00\n\n<5교시>\n02:00 ~ 2:50\n\n<6교시>\n03:00 ~ 3:50\n\n<7교시>\n04:00 ~ 4:50", color=0x00ff56)
        embed.set_author(name="수원정보과학고등학교 시정표", url=" ")
        await message.channel.send(embed=embed)
        
    if content.startswith("!도움말"):
        embed=discord.Embed(description="```\n!자기소개\n!시간표\n!월시간표\n!화시간표\n!수시간표\n!목시간표\n!금시간표\n!시정표\n!코드업 (문제번호)\n!청소 (삭제할 메시지 갯수)\n!공지 (공지내용)\n!오피지지\n!롤체지지\n!옵지 (검색할 유저 닉네임)\n!롤체 (검색할 유저 닉네임)\n!깃헙 (검색할 사람 아이디)\n!시간\n!CBT\n```", color=0x00ff55)
        embed.set_author(name="<<명령어>>", url="")
        await message.channel.send(embed=embed)

    if content.startswith("!코드업"):
        nick = message.content[6:]
        embed=discord.Embed(description="코드업 {} 바로가기\nhttps://www.codeup.kr/problem.php?id={}".format(nick,nick), color=0x00ff56)
        embed.set_author(name="<<{}번 문제>>".format(nick))
        await message.channel.send(embed=embed)
    
    if message.content.startswith ("!청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님에 의해 삭제 되었습니다".format(amount, message.author), color=0x00ff56)
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))
                
    if message.content.startswith ("!공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel('')
            embed = discord.Embed(title="**공지사항 제목*", description="\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="공지 작성자 : {}".format(message.author))
            await message.channel.send ("@everyone", embed=embed)
            await message.author.send("```*[ BOT 자동 알림 ]* | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}```".format(channel, message.author, notice))
       
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

    if content.startswith("!롤체지지"):
        embed=discord.Embed(description="https://lolchess.gg/meta", color=0x00ff56)
        embed.set_author(name="<<롤체지지>>", url="https://lolchess.gg/meta")
        await message.channel.send(embed=embed)

    if content.startswith("!CBT"):
        embed=discord.Embed(description="https://www.comcbt.com/xe/c2/4400733", color=0x00ff56)
        embed.set_author(name="<<CBT>>", url="https://www.comcbt.com/xe/c2/4400733")
        await message.channel.send(embed=embed)
    
    if content.startswith("!오피지지"):
        embed=discord.Embed(description="https://op.gg", color=0x00ff56)
        embed.set_author(name="<<오피지지>>",url="https://op.gg")
        await message.channel.send(embed=embed)
        
    if(message.content == "!시간"):
        await message.channel.send(embed=discord.Embed(title="Time", timestamp=datetime.datetime.utcnow()))
        
    if content.startswith("!옵지"):
        nick = message.content[4:]
        embed=discord.Embed(description="오피지지 {} 바로가기\nhttps://www.op.gg/summoner/userName={}".format(nick,nick), color=0x00ff56)
        embed.set_author(name="<<{}>>".format(nick))
        await message.channel.send(embed=embed)
        
    if content.startswith("!롤체"):
        nick = message.content[4:]
        embed=discord.Embed(description="롤체지지 {} 바로가기\nhttps://lolchess.gg/profile/kr/{}".format(nick,nick), color=0x00ff56)
        embed.set_author(name="<<{}>>".format(nick))
        await message.channel.send(embed=embed)
    
    if content.startswith("!깃헙"):
        nick = message.content[4:]
        embed=discord.Embed(description="깃허브 {} 바로가기\nhttps://github.com/{}".format(nick,nick), color=0x00ff56)
        embed.set_author(name="<<{}>>".format(nick))
        await message.channel.send(embed=embed)

    #-------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------------------
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)