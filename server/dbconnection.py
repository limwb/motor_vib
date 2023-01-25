from pymongo import MongoClient

class MongoDB():
    def __init__(self):
        self.client = MongoClient(host='localhost', port=27017)
        self.db = self.client['test']  # test2 : db이름(생성)
        self.col = self.db['data']

    def insert_data(self, data):
        _ = self.db['data'].insert_one(data)

    def get_all_data(self):
        data = []
        for d in self.col.find():
            data.append(d)
            # print(d)
        return data