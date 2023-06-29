# fileName: nabilanavab/instaMate/database.py
# copyright ©️ 2023 nabilanavab

import datetime
from pymongo import MongoClient
from bot.util import config


class Database:

    def __init__(self, uri, database_name):
        self.client = MongoClient(uri)
        self.db = self.client[database_name]
        self.col = self.db.insta

    def new_user(self, id, name):
        return dict(id=id,
                    name=name,
                    join_date=datetime.date.today().isoformat())

    def delete_user(self, user_id):
        self.col.delete_many({'id': int(user_id)})

    def is_user_exist(self, id):
        user = self.col.find_one({'id': int(id)})
        return bool(user)

    def add_user(self, id, name):
        user = self.new_user(id, name)
        self.col.insert_one(user)

    def get_banned(self):
        users = self.col.find({"banned": {"$regex": "^(?!\s*$).+"}})
        b_users = [user['id'] for user in users]
        return b_users

    def set_key(self, id, key, value):
        if value is None:
            return self.col.update_one({'id': id}, {'$unset': {f'{key}': ""}})
        else:
            return self.col.update_one({'id': id}, {'$set': {f'{key}': value}})

    def get_key(self, id, key):
        user = self.col.find_one({'id': int(id)})
        return user.get(f'{key}', None)

    def get_user_data(self, id) -> dict:
        user = self.col.find_one({'id': int(id)})
        return user or None

    def get_all_users(self):
        return self.col.find({})

    def total_users_count(self):
        count = self.col.count_documents({})
        return count


if config.MONGODB_URI:
    db = Database(config.MONGODB_URI, "nabilanavab")

# Author : @nabilanavab
