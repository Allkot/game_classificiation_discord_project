import discord
import random
from discord.ext import commands
from classification import game_detect

# Переменная intents - хранит привилегии бота
intents = discord.Intents.all()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')



@bot.command()
async def about(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def Guess_game(ctx):
    if ctx.message.attachments:
        for i in ctx.message.attachments:
            file_name = i.filename
            urk = i.url
            await i.save(f"./{file_name}")
            inform = game_detect(f"./{file_name}")
            index = inform[2]
            delete = '''\\n'''
            class_names = inform[0]
            for i in delete:
                class_names = class_names.replace(i,"")
            await ctx.send(f'========================================')
            await ctx.send(f'=======Название игры: {class_names}')
            await ctx.send(f'=======Вероятность: {inform[1]}%=======')
            await ctx.send(f'=======================================')
            if index == 0:
                await ctx.send('''
                RELEASE DATE:10 Nov, 2015
            DEVELOPER:Bethesda Game Studios
            PUBLISHER:Bethesda Softworks
            Popular user-defined tags for this product:
            Open World ,Post-apocalyptic ,Singleplayer ,RPG''')
            elif index == 1:
                await ctx.send('''
                RELEASE DATE:16 Nov, 2004
            DEVELOPER:Valve
            PUBLISHER:Valve
            Popular user-defined tags for this product:
            FPS , Action , Sci-fi ,Classic ,Singleplayer ''')
            elif index == 2:
                await ctx.send('''
                Дата выпуска: 27 июля 2010 г.
            Разработчик: Blizzard Entertainment
            Режим: Многопользовательская игра
            Жанры: Стратегия в реальном времени, Экшен, Приключенческая игра ''')
    else:
        await ctx.send("no image found")

    
bot.run("MTExNDE1NjY5NzQzOTcxMTIzMg.GMNH3k.9_PHOM6OJ7Up36BkAYG95iDrAUlL6DsXfS4xuw")