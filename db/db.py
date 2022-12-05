#db part
import pymongo

HOST = "localhost"
PORT = 27017

def save_in_db(LN, N, P, T, M):
    client = pymongo.MongoClient(HOST, PORT)
    db = client['Project']
    series_collection = db['Project']

    new_doc = {"Last name": LN, "Name": N, "Patronymic": P, "Telephone": T, "Message": M}
    id_ = series_collection.insert_one(new_doc)

    print("Query saved in DB")




