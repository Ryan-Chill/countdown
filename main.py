import os
import discord
from dotenv import load_dotenv
import keep_alive
import time
import datetime
from PIL import Image, ImageFont, ImageDraw 

load_dotenv()
token = os.getenv('discordbottoken')

client = discord.Client()

#Friday, September 30, 2022 03:00:00 Timezone: Etc/GMT-3 (UTC+03:00)
def countdown(stop):
    difference = stop - datetime.datetime.now()
    count_hours, rem = divmod(difference.seconds, 3600)
    count_minutes, count_seconds = divmod(rem, 60)
    for i in [difference.days, count_hours, count_minutes, count_seconds]:
      if i <= 0:
        i = 0
    return f"{difference.days:03d}", f"{count_hours:02d}", f"{count_minutes:02d}" # You may add `f"{count_seconds:02d}"` if needed



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
  if message.content.startswith('$cd'):
    endtime = datetime.datetime(2022, 9, 30, 0, 0, 0)
    end_d, end_h, end_m = countdown(endtime)
    font = ImageFont.truetype("Blue Yellow.ttf", 120)
    cd_image = Image.open("countdown_template.png")
    edit_cd = ImageDraw.Draw(cd_image)
    edit_cd.text((60,203), str(end_d), font=font)
    edit_cd.text((335,203), str(end_h), font=font)
    edit_cd.text((577,203), str(end_m), font=font)
    cd_image.save("edited_cd.png")
    await message.channel.send(file=discord.File('edited_cd.png'))
    

keep_alive.keep_alive()
client.run(token)
