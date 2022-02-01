from ast import alias
from PIL import Image
import pytesseract
import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

load_dotenv()

vish = commands.Bot(command_prefix=commands.when_mentioned_or("."))


@vish.command(aliases=['bruh'])
async def ocr(ctx):
    await ctx.channel.send('>>> Processing image...')
    for i in ctx.message.attachments:
        await i.save(i.filename)
        text = pytesseract.image_to_string(Image.open(i.filename))
        os.remove(i.filename)
        await ctx.channel.send('```' + text + '```')


@vish.event
async def on_ready():
    print('We have logged in as {0.user}'.format(vish))


# @vish.event
# async def on_message(message):
#     if message.author == vish.user:
#         return

#     if message.content.startswith('.ocr'):
#         await message.channel.send('>>> Processing image...')
#         for i in message.attachments:
#             await i.save(i.filename)
#             text = pytesseract.image_to_string(Image.open(i.filename))
#             os.remove(i.filename)
#             await message.channel.send('```' + text + '```')


vish.run(os.getenv('TOKEN'))
