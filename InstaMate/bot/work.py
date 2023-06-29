# fileName: nabilanavab/instaMate/bot/work.py
# copyright ©️ 2023 nabilanavab

import os
import shutil


class Work():

    RM_WORK = []
    HOME_DIR = os.path.abspath(os.getcwd())
    LOG_FILE = F"{HOME_DIR}/socialDL.log"
    WORKING_DIR = f"{HOME_DIR}/nabilanavab"
    WORK_IN_PROGRESS = []

    @staticmethod
    def restart_works():
        if os.path.exists(Work.WORKING_DIR):
            for user_id in os.listdir(Work.WORKING_DIR):
                Work.RM_WORK.append(
                    int(user_id) if user_id.isdigit() else user_id)
            shutil.rmtree(Work.WORKING_DIR)
        os.makedirs("nabilanavab")

    @staticmethod
    def create_work(user_id):
        if Work.check_work(user_id):
            return False
        dir = f"{Work.WORKING_DIR}/{user_id}"
        os.makedirs(dir)
        return dir

    @staticmethod
    def check_work(user_id):
        dir = f"{Work.WORKING_DIR}/{user_id}"
        return path if os.path.exists(dir) else False

    @staticmethod
    def delete_work(user_id):
        dir = f"{Work.WORKING_DIR}/{user_id}"
        return shutil.rmtree(dir, ignore_errors=True)

# Author : @nabilanavab
