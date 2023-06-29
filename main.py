from bot import bot
from bot.work import Work
from logger import logger
from bot.util import config
from handlers import (isUser, start_handler, url_handler, force_handler,
                      refresh_handler)


bot.add_custom_filter(isUser())

@bot.message_handler(is_user=False)
def forceSubscription(message):
    return force_handler.force_handler(message)


@bot.message_handler(commands=["start"])
def start(message):
    return start_handler.start_handler(message)


@bot.message_handler(content_types=['text'])
def url(message):
    return url_handler.url_handler(message)


@bot.callback_query_handler(func=lambda call: call.data == 'refresh')
def refresh(call):
    return refresh_handler.refresh_handler(call)


if __name__ == "__main__":
    work = Work().restart_works()
    logger.debug('bot restarted..')
    bot.polling()
