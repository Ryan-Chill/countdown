import os
import discord
from dotenv import load_dotenv
import keep_alive
import datetime #required for countdown calculation
from PIL import Image, ImageFont, ImageDraw #required for image import, image font import, editing image

load_dotenv()
token = os.getenv('discordbottoken')

client = discord.Client()

#Friday, September 30, 2022 00:00:00 Timezone: Etc/GMT+0 (UTC+00:00) <- estimated kusanali arrival
#function takes in ending datetime, returns countdown (ending days, ending hours, ending minutes as separate variables)
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
    endtime = datetime.datetime(2022, 9, 30, 0, 0, 0) #modifying end date (you may modify it according to timezone for different coding platforms)
    end_d, end_h, end_m = countdown(endtime) #you may add `end_s` if needed
    font = ImageFont.truetype("Blue Yellow.ttf", 120) #importing font
    cd_image = Image.open("countdown_template.png") #importing countdown picture template
    edit_cd = ImageDraw.Draw(cd_image) #start editing picture with our countdown variables
    edit_cd.text((60,203), str(end_d), font=font) #you may modify their coordinates if template was changed
    edit_cd.text((335,203), str(end_h), font=font)
    edit_cd.text((577,203), str(end_m), font=font)
    #edit_cd.text((x,y), str(end_s), font=font) #this may be enabled if seconds countdown is required
    cd_image.save("edited_cd.png") #save the edited picture
    await message.channel.send(file=discord.File('edited_cd.png')) #call the edited picture file and send it in channel
    

keep_alive.keep_alive()
client.run(token)
