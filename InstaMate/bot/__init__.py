# fileName: nabilanavab/instaMate/bot/__init__.py
# copyright ©️ 2023 nabilanavab

import telebot
from .util import config
from telebot import types

bot = telebot.TeleBot(config.API_TOKEN, parse_mode=None)


try:
    _bot = bot.get_me()
    
    class BotInfo:
        bot_id = _bot.id
        bot_first_name = _bot.first_name
        bot_username = _bot.username
except Exception as Error:
    pass

# Author : @nabilanavab
