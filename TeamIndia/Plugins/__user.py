from TeamIndia.functions.users import *



__help__ = "Click on below buttons and check amazing tools for users."

  # no help string

__button__ = [ InlineKeyboardButton(text="Horoscope", callback_data="indiauser_"),
            InlineKeyboardButton(text="AFK", callback_data="indiauserafk_"),
            InlineKeyboardButton(text="About", callback_data="indiauserabout_"),

] 
__buttons__ = [InlineKeyboardButton(text="Info", callback_data="indiauserinfo_"), 
              InlineKeyboardButton(text="History", callback_data="indiauserhistory_"),
              InlineKeyboardButton(text="Extra", callback_data="indiauserextra_"),
]


__mod_name__ = "User"


dispatcher.add_handler(user_callback_handler)
dispatcher.add_handler(user_afk_callback_handler)
dispatcher.add_handler(user_about_callback_handler)
dispatcher.add_handler(user_info_callback_handler)
dispatcher.add_handler(user_histroy_callback_handler)
dispatcher.add_handler(user_extra_callback_handler)
