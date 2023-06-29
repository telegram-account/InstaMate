# fileName: nabilanavab/instaMate/handlers/url_handler.py
# copyright ©️ 2023 nabilanavab

import re
import requests
from bot import *
from logger import logger
from bs4 import BeautifulSoup
from bot.info import userInfo


def UrlConverter(text: str) -> list:
    try:
        urls = re.findall(r'(https?://\S+)', text)

        for index, url in enumerate(urls):
            if 'instagram.com' in url:
                urls[index] = "https://ddinstagram.com/" + url.split('/', 3)[3]
            elif 'twitter.com' in url:
                urls[index] = "https://fxtwitter.com/" + url.split('/', 3)[3]
            elif 'tiktok.com' in url:
                urls[index] = "https://vxtwitter.com/" + url.split('/', 3)[3]

        return urls if not len(urls) == 0 else None
    except Exception:
        return None


def GenerateCaption(url: str) -> str:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        if 'instagram.com' in url:
            title = soup.find('meta', attrs={'name':
                                             'twitter:title'})['content']
            userlink = f"https://www.instagram.com/{title}"
            desc = soup.find('meta', attrs={'name': 'description'})['content']
        elif 'twitter.com' in url:
            title = soup.find('meta', attrs={'property':
                                             'twitter:title'})['content']
            userlink = f'https://twitter.com/' + \
                       soup.find('meta', attrs={'property': 'twitter:creator'})['content']
            desc = soup.find('meta', attrs={'property':
                                            'og:description'})['content']

        meta_tag = soup.find('meta', attrs={"property": "og:video:type"})
        if meta_tag is not None and 'content' in meta_tag.attrs and meta_tag[
                'content'] == "video/mp4":
            _type = 'video'
        else:
            if 'instagram.com' in url:
                _type = url
            elif 'twitter.com' in url:
                _type = soup.find('meta', attrs={"property":
                                                 "og:image"})['content']

        return _type, userlink, f'{desc}\n\n<b>👤: <a href="{userlink}">{title}</a> </b>'
    except Exception as Error:
        logger.exception(Error, exc_info=True)
        return False, False, False


def url_handler(message):
    try:
        urls = UrlConverter(message.text)
        if not urls:
            return
        reply = bot.reply_to(message=message,
                             text='`processing..`',
                             parse_mode="Markdown")
        for url in urls:
            _type, userlink, caption = GenerateCaption(url=url)

            if (_type and userlink) == caption:
                raise 'Error'

            bot.send_chat_action(message.chat.id, 'upload_video')
            key = types.InlineKeyboardMarkup()
            key.add(
                types.InlineKeyboardButton("🎈 View Profile 🎈", url=userlink))
            key.add(types.InlineKeyboardButton("👀 View Post 👀", url=url))
            if _type == 'video':
                logger.debug(url)
                file_id = bot.send_video(video=url,
                                         chat_id=message.chat.id,
                                         caption=caption,
                                         reply_markup=key,
                                         parse_mode="Html")
            else:
                file_id = bot.send_photo(photo=_type,
                                         chat_id=message.chat.id,
                                         caption=caption,
                                         reply_markup=key,
                                         parse_mode="Html")
            userInfo.sendLogFileMsg(message, file_id, url)
        bot.delete_message(message.chat.id, reply.id)

    except Exception as Error:
        logger.exception(Error, exc_info=True)
        if message.chat.type != 'private':
            return bot.delete_message(message.chat.id, reply.id)
        bot.edit_message_text(
            text=
            "``` can't fetch data..\n\nNB: i cant fetch videos from private links :)```",
            chat_id=message.chat.id,
            message_id=reply.id,
            parse_mode="Markdown")

# Author : @nabilanavab
