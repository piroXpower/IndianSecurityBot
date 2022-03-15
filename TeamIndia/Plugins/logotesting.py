import os 
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from AliciaRobot.events import register
from AliciaRobot import telethn as bot

@register(pattern="^/mlogo ?(.*)")
async def makelogo(event):
        quew = event.pattern_match.group(1)
        hsize = 1.5
        dhsize = 1.3
            
        if not quew:
           await event.reply('Provide Some Text To Draw and Reply to any Image/Sticker! Example: /logo <your name>')
           return
        else:
           pass
        msg = await event.reply('Creating your logo...wait!')

        allFonts = [
            "font(1).otf", "font(2).otf", "font(3).otf", "font(4).otf","font(5).otf","font(6).otf", "font(7).otf", "font(8).otf",
            "font(9).otf", "font(10).otf", "font(11).otf","font(12).otf", "font(13).otf", "font(14).otf", "font(15).otf", "font(16).otf",
            "font(17).otf", "font(18).otf",
            "tfont(1).ttf", "tfont(2).ttf", "tfont(3).ttf", "tfont(4).ttf", "tfont(5).ttf","tfont(6).ttf", "tfont(7).ttf", "tfont(8).ttf",
            "tfont(9).ttf", "tfont(10).ttf", "tfont(11).ttf", "tfont(12).ttf", "tfont(13).ttf","tfont(14).ttf", "tfont(15).ttf", "tfont(16).ttf",
            "tfont(17).ttf", "tfont(18).ttf", "tfont(19).ttf", "tfont(20).ttf", "tfont(21).ttf", "tfont(22).ttf", "tfont(23).ttf", "tfont(24).ttf",
            "tfont(25).ttf", "tfont(26).ttf", "tfont(27).ttf", "tfont(28).ttf", "tfont(29).ttf", "tfont(30).ttf", "tfont(31).ttf", "tfont(32).ttf",
            "tfont(33).ttf", "tfont(34).ttf", "tfont(35).ttf", "tfont(36).ttf","tfont(37).ttf", "tfont(38).ttf", "tfont(39).ttf", "tfont(40).ttf",
            "tfont(41).ttf", "tfont(42).ttf",  
            ]
        randFont = random.choice(allFonts)
        res = f"https://github.com/H1M4N5HU0P/AliciaFonts/raw/main/{randFont}"
        response = requests.get(res)
        urlfont = BytesIO(response.content)
        
        reply_message = await event.get_reply_message()
        
        file = await bot.download_media(reply_message)

        img = Image.open(file)


        blueimg = img.filter(ImageFilter.BoxBlur(1))

        try:
            text = quew
            if ";" in text:
                upper_text, lower_text = text.split(";")
                upper_text = upper_text.strip() 
                lower_text = lower_text.strip()
            else:
               upper_text = text
               lower_text = ""
            

            draw = ImageDraw.Draw(blueimg)
            imgSize = blueimg.size


            if upper_text:
        
                  
                  fontSize = int(imgSize[1] / 5)
                  image_widthz, image_heightz = img.size    
                  font = ImageFont.truetype(urlfont, fontSize)
                  textSize = font.getsize(upper_text)
                  while textSize[0] > imgSize[0] - 100:
                     fontSize -= 1
                     font = ImageFont.truetype(urlfont, fontSize)
                     textSize = font.getsize(upper_text)
                  w, h = draw.textsize(upper_text, font=font)
                  h += int(h*0.5)
                  image_width, image_height = blueimg.size
                  x = (image_widthz-w)/2
                  y= ((image_heightz-h)/hsize+6)
                  draw.text((x, y), upper_text, font=font, fill="White", stroke_width=4, stroke_fill="black")
        
                  
              
            if lower_text:
        
                  fontSize = int(imgSize[1] / 14)
                  image_widthz, image_heightz = img.size
                  font = ImageFont.truetype(urlfont, fontSize)
                  textSize = font.getsize(lower_text)
                  while textSize[0] > imgSize[0] - 100:
                     fontSize -= 1
                     font = ImageFont.truetype(urlfont, fontSize)
                     textSize = font.getsize(lower_text)
                  w, h = draw.textsize(lower_text, font=font)
                  h += int(h*0.5)
                  image_width, image_height = blueimg.size
                  x = (image_widthz-w)/2
                  y= ((image_heightz-h)/dhsize+6)
                  
                  draw.text((x, y), lower_text, font=font, fill="white", stroke_width=1, stroke_fill="black")
                  
            fname2 = "LogoByAliciaRobot.png"
            blueimg.save(fname2, "png")
            await bot.send_file(event.chat_id, fname2, caption="Made By @AliciaGroup_bot")
            if os.path.exists(fname2):
               os.remove(fname2)
            if os.path.exists(randFont):
               os.remove(randFont)


    

        except Exception as e:
            await msg.edit(f'Error Report @MafiaBot_Support, {e} \nmaybe error with font {randFont}, you should try again.')
