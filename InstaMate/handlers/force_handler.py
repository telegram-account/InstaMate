# fileName: nabilanavab/instaMate/handlers/force_handler.py
# copyright ©️ 2023 nabilanavab

from bot import *
from logger import logger
from bot.util import config
from bot.info import userInfo
from chatLog import refreshMessage, startMessage


def force_handler(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        reply = bot.send_photo(chat_id=message.chat.id,
                               photo=startMessage.PHOTO,
                               reply_to_message_id=message.id,
                               caption='.',
                               parse_mode="Markdown")
        bot.edit_message_caption(caption='..',
                                 chat_id=message.chat.id,
                                 message_id=reply.id)

        bot.edit_message_caption(caption=refreshMessage.REFRESH_MESSAGE,
                                 chat_id=message.chat.id,
                                 message_id=reply.id,
                                 reply_markup=refreshMessage.BUTTON,
                                 parse_mode="Markdown")

        if config.MONGODB_URI:
            userInfo.sndUsrLogMsg(message)

    except Exception as Error:
        logger.debug(Error, exc_info=True)

# Author : @nabilanavab
