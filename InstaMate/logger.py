# fileName: nabilanavab/instaMate/logger.py
# copyright ©️ 2023 nabilanavab

import logging
from bot.work import Work

logger = logging.getLogger(__name__)
logging.getLogger("urllib3").setLevel(logging.ERROR)

logging.basicConfig(
    filemode="a",
    level=logging.DEBUG,
    datefmt='%d-%b-%y %H:%M:%S',
    filename=Work.LOG_FILE if
    (Work.LOG_FILE and Work.LOG_FILE[-4:] == ".log") else None,
    format="[%(asctime)s - %(name)s] : %(levelname)s - %(message)s",
)

# Author : @nabilanavab
