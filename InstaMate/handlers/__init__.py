# fileName: nabilanavab/instaMate/handlers/__init__.py
# copyright ©️ 2023 nabilanavab

from bot import *
from logger import logger
from bot.util import config


class isUser(telebot.custom_filters.SimpleCustomFilter):

    key = 'is_user'

    def check(self, message):
        try:
            if not config.FORCE_SUB: return True
            userStatus = bot.get_chat_member(config.FORCE_SUB,
                                             message.from_user.id).status
            return True if userStatus in [
                'administrator', 'creator', 'member'
            ] else False
        except Exception:
            return False

# Author : @nabilanavab
