# fileName: nabilanavab/instaMate/chatLog.py
# copyright ©️ 2023 nabilanavab

from bot import *
from bot.info import Info
from bot.util import config


class startMessage:
    PHOTO = "https://graph.org/file/8baa89dc727d67d9be193.jpg"
    START_MESSAGE = '''**Hey there ! Welcome to InstaMate Bot !**  
``` With my help, you can retrieve your favorite instagram, twitter posts in the most efficient and speedy manner possible. 😲```

_Just provide me with the post's URL, and I'll take care of the rest. Get ready to experience hassle-free and rapid downloads_ 😏'''
    BUTTON = types.InlineKeyboardMarkup()
    BUTTON.add(
        types.InlineKeyboardButton("😎 Contact Admin 😎", url=Info.owner_url))


class refreshMessage(object):
    REFRESH_MESSAGE = '''**Hey there ! Welcome to InstaMate Bot !**

``` Due to limited hosting resources, only members of this channel can enjoy its services.```

Join the link below and click on the _'♻ REFRESH ♻'_ button'''
    CB_ANSWER = 'Join the link below and click on the refresh button 🙂'
    BUTTON = types.InlineKeyboardMarkup()
    BUTTON.add(
        types.InlineKeyboardButton(
            "😎 JOIN CHANNEL 😎",
            url=
            f'https://telegram.dog/{config.FORCE_SUB[1:] if config.FORCE_SUB else ""}'
        ))
    BUTTON.add(
        types.InlineKeyboardButton("♻️ REFRESH ♻️", callback_data='refresh'))

# Author : @nabilanavab
