# fileName: nabilanavab/instaMate/bot/info.py
# copyright ©️ 2023 nabilanavab

from bot import *
from bot.util import config
from logger import logger

if config.MONGODB_URI:
    from .database import db


class Info(object):
    owner_id = 32453245
    owner_url = 't.me/nabilanavab'
    owner_name = 'nabil a navab'
    owner_username = 'nabilanavab'


class userInfo():

    @staticmethod
    def sndUsrLogMsg(message):
        if message.chat.type != 'private':
            return bot.send_message(
                chat_id=config.LOG_CHANNEL,
                text='#newUser_{0}_ @nabilanavab 🙂\n\n`{1}`'.format(
                    BotInfo.bot_username, message.chat.id),
                parse_mode="Html")
        if config.MONGODB_URI and not db.is_user_exist(message.from_user.id):
            db.add_user(message.from_user.id, message.from_user.first_name)
        elif not (config.LOG_CHANNEL and config.SEND_NEW_USER_MSG):
            return '🙂'
        else:
            return '🙂'
        key = types.InlineKeyboardMarkup()
        key.add(
            types.InlineKeyboardButton(
                "🙄 Ban User 🙄", callback_data=f'ban:{message.from_user.id}'))
        return bot.send_message(
            chat_id=config.LOG_CHANNEL,
            text='''#newUser_{0} @nabilanavab 🙂

userID            : {1}
viewProfile   : <a href="tg://user?id={1}">{2}</a>{3}'''.format(
                BotInfo.bot_username,
                message.from_user.id,
                message.from_user.first_name,
                f'\nUsername     : @{message.from_user.username}'
                if message.from_user.username else ' ',
            ),
            reply_markup=key,
            parse_mode="Html")

    @staticmethod
    def sendLogFileMsg(message, file_id, url):
        if not (config.LOG_CHANNEL and config.SEND_LOG_MESSAGE):
            return '🙂'
        key = types.InlineKeyboardMarkup()
        key.add(types.InlineKeyboardButton("👀 View Post 👀", url=f'{url}'))
        key.add(
            types.InlineKeyboardButton(
                "🙄 Ban User 🙄", callback_data=f'ban:{message.from_user.id}'))
        return bot.copy_message(
            config.LOG_CHANNEL,
            message.chat.id,
            file_id.id,
            parse_mode="Html",
            reply_markup=key,
            caption=file_id.caption + '''

#newPost_{0} @nabilanavab 🙂

userID            : {1}
viewProfile   : <a href="tg://user?id={1}">{2}</a>{3}'''.format(
                BotInfo.bot_username,
                message.from_user.id,
                message.from_user.first_name,
                f'\nUsername     : @{message.from_user.username}'
                if message.from_user.username else ' ',
            ),
        )

# Author : @nabilanavab
