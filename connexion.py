import json
from pymongo import MongoClient


class Query():
    def login_db(self):
        try: 
            with open('login.json') as json_data:
                data_dict = json.load(json_data)
                user = ("Guillaume",data_dict["Guillaume"])
        except:
            user = ("Stephane","Stephane")
        
        return user

    def conn(self):
        login_db = self.login_db()
        client = MongoClient("mongodb+srv://%s:%s@cluster0.bk25f.mongodb.net/Cluster0?retryWrites=true&w=majority"%(login_db[0], login_db[1]))  
        return client
    