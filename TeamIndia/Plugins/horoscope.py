import pyaztro

from AliciaRobot.events import register

ASTRO = ""


@register(pattern="^/hs (.*)")
async def astro(e):
    msg = await e.reply("Fetching data...")
    if not e.pattern_match.group(1):
        x = ASTRO
        if not x:
            await msg.edit("Not Found.")
            return
    else:
        try:
            x = e.pattern_match.group(1)
            horoscope = pyaztro.Aztro(sign=x)
            mood = horoscope.mood
            lt = horoscope.lucky_time
            desc = horoscope.description
            col = horoscope.color
            com = horoscope.compatibility
            ln = horoscope.lucky_number

            result = (
                f"**Horoscope for `{x}`**:\n"
                f"**Mood :** `{mood}`\n"
                f"**Lucky Time :** `{lt}`\n"
                f"**Lucky Color :** `{col}`\n"
                f"**Lucky Number :** `{ln}`\n"
                f"**Compatibility :** `{com}`\n"
                f"**Description :** `{desc}`\n"
            )

            await msg.edit(result)

        except Exception as e:
            await msg.edit(f"Sorry i haven't found anything!\nmaybe you have given a wrong sign name please check help of horoscope.\nError - {e}")

# __help__ = """
#  - /hs <sign> 
#  Usage: it will show horoscope of daily of your sign.
#  List of all signs - aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius and pisces.
# """

__mod_name__ = "Horoscope"

__button__ = ""
__buttons__ = ""