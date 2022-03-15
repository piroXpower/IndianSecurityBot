from AliciaRobot.functions.fun import *



__help__ = """We promise to keep you latest up-date with the latest technology on telegram. 
we updradge alicia everyday to simplifie use of telegram and give a better exprince to Users.

Click on below buttons and check amazing tools for Fun.
"""  # no help string

__button__ = [ InlineKeyboardButton(text="Memes", callback_data="aliciafun_"),
            InlineKeyboardButton(text="Emojis", callback_data="aliciafunemoji_"),
            InlineKeyboardButton(text="Games", callback_data="aliciafungames_"),

] 
__buttons__ = [InlineKeyboardButton(text="Couple", callback_data="aliciafuncouple_"), 
              InlineKeyboardButton(text="Karma", callback_data="aliciafunkarma_"),
]


__mod_name__ = "Fun"


dispatcher.add_handler(fun_callback_handler)
dispatcher.add_handler(fun_emoji_callback_handler)
dispatcher.add_handler(fun_games_callback_handler)
dispatcher.add_handler(fun_couple_callback_handler)
dispatcher.add_handler(fun_karma_callback_handler)
