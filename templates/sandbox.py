from pymongo import MongoClient

client = MongoClient("mongodb+srv://Guillaume:Yjgr65JvNeiyMAgl@cluster0.bk25f.mongodb.net/Cluster0?retryWrites=true&w=majority") 

conn = client.WWF.Compte.find({"user": {"$eq": "guillaume"}})
login = client.WWF.Compte

def compte(user, password):
    user = user
    password = password
    conn = client.WWF.Compte.find({"user": {"$eq": user}})
    for i in conn:
        item = i
    try: item
    except NameError: item = None
    if (item):
        global compte
        user=item["user"]
        if (password == item["user"]):
            password=item["password"]
            compte=(user, password)
            return compte
        else:
            return

print(compte("guillaume", "uillaume"))