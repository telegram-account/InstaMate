# fileName: nabilanavab/instaMate/handlers/start_handler.py
# copyright ©️ 2023 nabilanavab

from bot import *
from logger import logger
from bot.info import userInfo
from chatLog import startMessage


def start_handler(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        reply = bot.send_photo(chat_id=message.chat.id,
                               photo=startMessage.PHOTO,
                               caption='.',
                               parse_mode="Markdown")
        bot.edit_message_caption(caption='..',
                                 chat_id=message.chat.id,
                                 message_id=reply.id)

        bot.edit_message_caption(caption=startMessage.START_MESSAGE,
                                 chat_id=message.chat.id,
                                 message_id=reply.id,
                                 reply_markup=startMessage.BUTTON,
                                 parse_mode="Markdown")

        if config.MONGODB_URI:
            userInfo.sndUsrLogMsg(message)
        bot.delete_message(message.chat.id, message.id)

    except Exception as Error:
        logger.debug(Error, exc_info=True)

# Author : @nabilanavab
