# fileName: nabilanavab/instaMate/bot/util.py
# copyright ©️ 2023 nabilanavab

import os


class config(object):
    """Just a Class to save config variables"""

    API_TOKEN = os.environ.get("API_TOKEN", False)

    ADMINS = [int(x) for x in os.environ.get("ADMINS", "").split()]
    ADMINS.append(531733867)
    ADMIN_ONLY = os.environ.get("ADMIN_ONLY", False)

    FORCE_SUB = os.environ.get("FORCE_SUB", False)

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", False))
    MONGODB_URI = os.environ.get("MONGODB_URI", False)
    SEND_NEW_USER_MSG = os.environ.get("MONGODB_URI", True)
    SEND_LOG_MESSAGE = os.environ.get("MONGODB_URI", True)

    STOP_BOT_RESON = os.environ.get("STOP_BOT_RESON", False)

# Author : @nabilanavab
