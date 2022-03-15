import io
import textwrap
import random

from PIL import Image, ImageDraw, ImageFont
from AliciaRobot import telethn as client
from AliciaRobot.events import register


@register(pattern="/slet (.*)")
async def sticklet(event):
    sticktext = event.pattern_match.group(1)

    if not sticktext:
        await event.reply("`I need text to sticklet!`")
        return

    sticktext = textwrap.wrap(sticktext, width=10)
    sticktext = '\n'.join(sticktext)

    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230
    font = ImageFont.truetype("./AliciaRobot/resources/Chopsic.otf", size=fontsize)
    strkcolor = ["yellow", "red", "blue", "purple", "white"]

    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype("./AliciaRobot/resources/Chopsic.otf", size=fontsize)

    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(((512-width)/2,(512-height)/2), sticktext, font=font, fill=random.choice(strkcolor))

    image_stream = io.BytesIO()
    image_stream.name = "sticker.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)

    await event.client.send_file(event.chat_id, image_stream)
