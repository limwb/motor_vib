from pymongo import MongoClient

class MongoDB():
    def __init__(self):
        self.client = MongoClient(host='localhost', port=27017)
        self.db = self.client['ai_data_db']
        self.col = self.db['motor_vib']

    def insert_data(self, data):
        _ = self.db['motor_vib'].insert_one(data)

    def get_all_data(self):
        data = []
        for d in self.col.find():
            data.append(d)
            # print(d)
        return data