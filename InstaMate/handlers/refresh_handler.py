# fileName: nabilanavab/instaMate/handlers/refresh_handler.py
# copyright ©️ 2023 nabilanavab

from bot import *
from logger import logger
from chatLog import startMessage, refreshMessage
from .url_handler import url_handler


def refresh_handler(call):
    try:
        userId = call.message.reply_to_message.from_user.id
        userStatus = bot.get_chat_member(config.FORCE_SUB, userId).status
        subscribed = True if userStatus in [
            'administrator', 'creator', 'member'
        ] else False

        if not subscribed:
            return bot.answer_callback_query(call.id, refreshMessage.CB_ANSWER)

        if call.message.reply_to_message.text.startswith('/start'):
            bot.edit_message_caption(caption=startMessage.START_MESSAGE,
                                     chat_id=call.message.chat.id,
                                     message_id=call.message.id,
                                     reply_markup=startMessage.BUTTON,
                                     parse_mode="Markdown")
            return bot.delete_message(call.message.chat.id,
                                      call.message.reply_to_message.id)
        else:
            bot.delete_message(call.message.chat.id, call.message.id)
            url_handler(call.message)
    except Exception as Error:
        logger.debug(Error, exc_info=True)

# Author : @nabilanavab
