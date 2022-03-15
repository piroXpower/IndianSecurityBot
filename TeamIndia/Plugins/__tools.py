from AliciaRobot.functions.tools import *



__mod_name__ = "Tools"

__help__ = """We promise to keep you latest up-date with the latest technology on telegram. 
we updradge alicia everyday to simplifie use of telegram and give a better exprince to users.

Click on below buttons and check amazing tools for users.

"""
__button__ = [ InlineKeyboardButton(text="Barcode", callback_data="aliciatoolsbarcode_"),
            InlineKeyboardButton(text="CC-Check", callback_data="aliciatoolscc_"),
            InlineKeyboardButton(text="Telegraph", callback_data="aliciatoolstelegraph_"),

] 
__buttons__ = [InlineKeyboardButton(text="TTS/STT", callback_data="aliciatoolstts_"), 
              InlineKeyboardButton(text="Search", callback_data="aliciatoolsearch_"),
              InlineKeyboardButton(text="Extra", callback_data="aliciatools_"),
]



dispatcher.add_handler(tools_callback_handler)
dispatcher.add_handler(tools_barcode_callback_handler)
dispatcher.add_handler(tools_cc_callback_handler)
dispatcher.add_handler(tools_telegraph_callback_handler)
dispatcher.add_handler(tools_tts_callback_handler)
dispatcher.add_handler(tools_search_callback_handler)