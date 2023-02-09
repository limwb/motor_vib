from pymongo import MongoClient

class MongoDB():
    def __init__(self, db_name = 'ai_data_db', collection='motor_vib'):
        self.client = MongoClient(host='localhost', port=27017)
        self.db = self.client[db_name]
        self.col = self.db[collection]

    def insert_data(self, data):
        _ = self.col.insert_one(data)

    def get_all_data(self):
        data = []
        for d in self.col.find():
            data.append(d)
            # print(d)
        return data