from asyncio.exceptions import SendfileNotAvailableError
from asyncio.tasks import sleep
import discord
from discord import user
from discord.ext import commands
import asyncio
import sys
from discord.ext.commands import Bot
import datetime
import os
from discord.member import flatten_user
from discord.utils import get
#디스코드 토큰  icon_url= 'https://newsimg.hankookilbo.com/cms/articlerelease/2016/12/06/201612061853373206_1.jpg'

if __name__ == '__main__':
  py_ver = int(f"{sys.version_info.major}{sys.version_info.minor}")
  if py_ver > 37 and sys.platform.startswith('win'):
     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

#변수
app = commands.Bot(command_prefix='!')
now_datetime = datetime.datetime.now()


#아이콘 및 URL
valtan = ["https://cdn.discordapp.com/attachments/883667431795609611/885014829709017178/0e9de24eaafea4ae.jpg"
,'✔','✖','☑']
argos =['https://cdn.discordapp.com/attachments/883667431795609611/883667714105823242/62de4903e4d12423.jpg',
'✅','❎','➡']
viakis = ['https://cdn.discordapp.com/attachments/883667431795609611/885014828538810368/610827920d513856.jpg',
'🔴','🔵','🔺']
saten = ['https://cdn.discordapp.com/attachments/883667431795609611/885014809207246888/2ec252fbe4d50a6a.jpg',
'📌','❌','✉']
abralshoud = ['https://cdn.discordapp.com/attachments/883667431795609611/885014812701098004/c0c14229f7c4cac0.jpg',
"➕","➖",'🔼']
oreha = ['https://cdn.discordapp.com/attachments/883667431795609611/885025660718964786/7eb5450ac5157a14.png',
'👍','👎','👌']

#디스코드 봇 실행 코드
@app.event
async def on_ready():
    print('다음으로 로그인 합니다.')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Game(name="!"), activity=None)

#발탄 모집      
    @app.command()
    async def 발탄(ctx,*,title):
        valtan_list=[]
        
        embed=discord.Embed(title = "모집시작", description = title, color = discord.Color.random())
        embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
        embed.add_field (name = "참가", value = valtan_list, inline = False)
        embed.set_thumbnail(url=valtan[0])
        msg = await ctx.send (embed=embed)
        await msg.add_reaction(valtan[1])
        await msg.add_reaction(valtan[2])
        await msg.add_reaction(valtan[3])
        def check_emoji_1(reaction_2, user_2):
            return reaction_2.emoji == valtan[1] or reaction_2.emoji == valtan[2] or reaction_2.emoji == valtan[3] and user_2.bot == False
        while True:
            try:
                reaction_2, user_2 = await app.wait_for(event='reaction_add', check=check_emoji_1)
                await msg.delete()
                if str(reaction_2) == valtan[1]:
                    if str(user_2.name) in valtan_list:
                        await ctx.send("이미 있습니다.")
                    else:
                        valtan_list.append(user_2.name)
                if str(reaction_2) == valtan[2]:
                    if str(user_2.name) in valtan_list:
                        valtan_list.remove(user_2.name)
                    else:
                        await ctx.send("참가하지 않았습니다.")
                if str(reaction_2) == valtan[3]:
                    await ctx.send(f"발탄 모집 종료되었습니다. \n 제목{title} \n 참여인원 {valtan_list}")
            
                embed=discord.Embed(title = "모집시작", description = title, color = discord.Color.random())
                embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
                embed.add_field (name = "참가", value = valtan_list, inline = False)
                embed.set_thumbnail(url=valtan[0])
                msg = await ctx.send (embed=embed)
                await msg.add_reaction(valtan[1])
                await msg.add_reaction(valtan[2])
                await msg.add_reaction(valtan[3])   
            except asyncio.TimeoutError:
                await ctx.send("시간이 초과되었습니다.")
                return

#아르고스 모집      
    @app.command()
    async def 아르고스(ctx,*,title):
        argos_list=[]
        
        embed=discord.Embed(title = "모집시작", description = title, color = discord.Color.random())
        embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
        embed.add_field (name = "참가", value = argos_list, inline = False)
        embed.set_thumbnail(url=argos[0])
        msg = await ctx.send (embed=embed)
        await msg.add_reaction(argos[1])
        await msg.add_reaction(argos[2])
        await msg.add_reaction(argos[3])
        def check_emoji_1(reaction_2, user_2):
            return reaction_2.emoji == argos[1] or reaction_2.emoji == argos[2] or reaction_2.emoji == argos[3] and user_2.bot == False
        while True:
            try:
                reaction_2, user_2 = await app.wait_for(event='reaction_add', check=check_emoji_1)
                await msg.delete()
                if str(reaction_2) == argos[1]:
                    if str(user_2.name) in argos_list:
                        await ctx.send("이미 있습니다.")
                    else:
                        argos_list.append(user_2.name)
                if str(reaction_2) == argos[2]:
                    if str(user_2.name) in argos_list:
                        argos_list.remove(user_2.name)
                    else:
                        await ctx.send("참가하지 않았습니다.")
                if str(reaction_2) == argos[3]:
                    await ctx.send(f"아르고스 모집 종료되었습니다. \n 제목{title} \n 참여인원 {argos_list}")
            
                embed=discord.Embed(title = "모집시작", description = title, color = discord.Color.random())
                embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
                embed.add_field (name = "참가", value = argos_list, inline = False)
                embed.set_thumbnail(url=argos[0])
                msg = await ctx.send (embed=embed)
                await msg.add_reaction(argos[1])
                await msg.add_reaction(argos[2])
                await msg.add_reaction(argos[3])   
            except asyncio.TimeoutError:
                await ctx.send("시간이 초과되었습니다.")
                return

#비아키스 모집      
    @app.command()
    async def 비아키스(ctx,*,title):
        viakis_list=[]
        
        embed=discord.Embed(title = "모집시작", description = title, color = discord.Color.random())
        embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
        embed.add_field (name = "참가", value = viakis_list, inline = False)
        embed.set_thumbnail(url=viakis[0])
        msg = await ctx.send (embed=embed)
        await msg.add_reaction(viakis[1])
        await msg.add_reaction(viakis[2])
        await msg.add_reaction(viakis[3])
        def check_emoji_1(reaction_2, user_2):
            return reaction_2.emoji == viakis[1] or reaction_2.emoji == viakis[2] or reaction_2.emoji == viakis[3] and user_2.bot == False
        while True:
            try:
                reaction_2, user_2 = await app.wait_for(event='reaction_add', check=check_emoji_1)
                await msg.delete()
                if str(reaction_2) == viakis[1]:
                    if str(user_2.name) in viakis_list:
                        await ctx.send("이미 있습니다.")
                    else:
                        viakis_list.append(user_2.name)
                if str(reaction_2) == viakis[2]:
                    if str(user_2.name) in viakis_list:
                        viakis_list.remove(user_2.name)
                    else:
                        await ctx.send("참가하지 않았습니다.")
                if str(reaction_2) == viakis[3]:
                    await ctx.send(f"비아키스 모집 종료되었습니다. \n 제목{title} \n 참여인원 {viakis_list}")
            
                embed=discord.Embed(title = "모집시작", description = title, color = discord.Color.random())
                embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
                embed.add_field (name = "참가", value = viakis_list, inline = False)
                embed.set_thumbnail(url=viakis[0])
                msg = await ctx.send (embed=embed)
                await msg.add_reaction(argos[1])
                await msg.add_reaction(argos[2])
                await msg.add_reaction(argos[3])   
            except asyncio.TimeoutError:
                await ctx.send("시간이 초과되었습니다.")
                return

#아브렐슈드 모집      
    @app.command()
    async def 아브렐슈드(ctx,*,title):
        abralshoud_list=[]
        
        embed=discord.Embed(title = "모집시작", description = title, color = discord.Color.random())
        embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
        embed.add_field (name = "참가", value = abralshoud_list, inline = False)
        embed.set_thumbnail(url=viakis[0])
        msg = await ctx.send (embed=embed)
        await msg.add_reaction(abralshoud[1])
        await msg.add_reaction(abralshoud[2])
        await msg.add_reaction(abralshoud[3])
        def check_emoji_1(reaction_2, user_2):
            return reaction_2.emoji == abralshoud[1] or reaction_2.emoji == abralshoud[2] or reaction_2.emoji == abralshoud[3] and user_2.bot == False
        while True:
            try:
                reaction_2, user_2 = await app.wait_for(event='reaction_add', check=check_emoji_1)
                await msg.delete()
                if str(reaction_2) == abralshoud[1]:
                    if str(user_2.name) in abralshoud_list:
                        await ctx.send("이미 있습니다.")
                    else:
                        abralshoud_list.append(user_2.name)
                if str(reaction_2) == abralshoud[2]:
                    if str(user_2.name) in abralshoud_list:
                        abralshoud_list.remove(user_2.name)
                    else:
                        await ctx.send("참가하지 않았습니다.")
                if str(reaction_2) == abralshoud[3]:
                    await ctx.send(f"아브렐슈드 모집 종료되었습니다. \n 제목{title} \n 참여인원 {abralshoud_list}")

                embed=discord.Embed(title = "모집시작", description = title, color = discord.Color.random())
                embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
                embed.add_field (name = "참가", value = abralshoud_list, inline = False)
                embed.set_thumbnail(url=abralshoud[0])
                msg = await ctx.send (embed=embed)
                await msg.add_reaction(abralshoud[1])
                await msg.add_reaction(abralshoud[2])
                await msg.add_reaction(abralshoud[3])   
            except asyncio.TimeoutError:
                await ctx.send("시간이 초과되었습니다.")
                return

#오레하 모집      
    @app.command()
    async def 오레하(ctx,*,title):
        oreha_list=[]
        
        embed=discord.Embed(title = "모집시작", description = title, color = discord.Color.random())
        embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
        embed.add_field (name = "참가", value = oreha_list, inline = False)
        embed.set_thumbnail(url=oreha[0])
        msg = await ctx.send (embed=embed)
        await msg.add_reaction(oreha[1])
        await msg.add_reaction(oreha[2])
        await msg.add_reaction(oreha[3])
        def check_emoji_1(reaction_2, user_2):
            return reaction_2.emoji == oreha[1] or reaction_2.emoji == oreha[2] or reaction_2.emoji == oreha[3] and user_2.bot == False
        while True:
            try:
                reaction_2, user_2 = await app.wait_for(event='reaction_add', check=check_emoji_1)
                await msg.delete()
                if str(reaction_2) == oreha[1]:
                    if str(user_2.name) in oreha_list:
                        await ctx.send("이미 있습니다.")
                    else:
                        oreha_list.append(user_2.name)
                if str(reaction_2) == oreha[2]:
                    if str(user_2.name) in oreha_list:
                        oreha_list.remove(user_2.name)
                    else:
                        await ctx.send("참가하지 않았습니다.")
                if str(reaction_2) == oreha[3]:
                    await ctx.send(f"오레하 모집 종료되었습니다. \n 제목{title} \n 참여인원 {oreha_list}")
            
                embed=discord.Embed(title = "모집시작", description = title, color = discord.Color.random())
                embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
                embed.add_field (name = "참가", value = oreha_list, inline = False)
                embed.set_thumbnail(url=oreha[0])
                msg = await ctx.send (embed=embed)
                await msg.add_reaction(oreha[1])
                await msg.add_reaction(oreha[2])
                await msg.add_reaction(oreha[3])   
            except asyncio.TimeoutError:
                await ctx.send("시간이 초과되었습니다.")
                return

#쿠크세이튼 모집      
    @app.command()
    async def 쿠크세이튼(ctx,*,title):
        saten_list=[]
        
        embed=discord.Embed(title = "모집시작", description = title, color = discord.Color.random())
        embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
        embed.add_field (name = "참가", value = saten_list, inline = False)
        embed.set_thumbnail(url=saten[0])
        msg = await ctx.send (embed=embed)
        await msg.add_reaction(saten[1])
        await msg.add_reaction(saten[2])
        await msg.add_reaction(saten[3])
        def check_emoji_1(reaction_2, user_2):
            return reaction_2.emoji == saten[1] or reaction_2.emoji == saten[2] or reaction_2.emoji == saten[3] and user_2.bot == False
        while True:
            try:
                reaction_2, user_2 = await app.wait_for(event='reaction_add', check=check_emoji_1)
                await msg.delete()
                if str(reaction_2) == saten[1]:
                    if str(user_2.name) in saten_list:
                        await ctx.send("이미 있습니다.")
                    else:
                        saten_list.append(user_2.name)
                if str(reaction_2) == saten[2]:
                    if str(user_2.name) in saten_list:
                        saten_list.remove(user_2.name)
                    else:
                        await ctx.send("참가하지 않았습니다.")
                if str(reaction_2) == saten[3]:
                    await ctx.send(f"오레하 모집 종료되었습니다. \n 제목{title} \n 참여인원 {saten_list}")
            
                embed=discord.Embed(title = "모집시작", description = title, color = discord.Color.random())
                embed.set_author(name= ctx.author.display_name, icon_url= ctx.author.avatar_url)
                embed.add_field (name = "참가", value = saten_list, inline = False)
                embed.set_thumbnail(url=saten[0])
                msg = await ctx.send (embed=embed)
                await msg.add_reaction(saten[1])
                await msg.add_reaction(saten[2])
                await msg.add_reaction(saten[3])   
            except asyncio.TimeoutError:
                await ctx.send("시간이 초과되었습니다.")
                return

#도움말
    @app.command()
    async def 도움말(ctx):
        embed=discord.Embed(title = "도움말", description = "공지", color = discord.Color.red())
        embed.add_field (name = "명령어", value = "봇 명령어가 더 간소화 되었습니다. \n ex) 발탄모집시작 -> 발탄 제목", inline = False)
        embed.add_field (name = "사용방법", value = "원하는 파티 모집에 가장 왼쪽부터 참가, 불참, 모집 포스팅 종료입니다. ", inline = False)
        embed.add_field (name = "주의사항", value = "여러개의 파티를 모집할 수 있으나, 같은 종류 \n ex) 발탄1파티모집 발탄2파티모집 은 불가합니다. \n 한 종류를 모두 모집한 후에 포스팅 종료를 하고 다른파티를 모집해주세요.", inline = False)
        embed.add_field (name = "봇 버전", value="2.0.0",inline=False)
        await ctx.send(embed=embed)