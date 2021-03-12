from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["mydb"]

coll = db["example"]

DATA=[
    {"_id":"10","name":"saurabh soni","age":"21","city":"fatehpur"},
    {"_id":"11","name":"gaurav soni","age":"22","city":"fatehpur"},
    {"_id":"13","name":"aman soni","age":"20","city":"fatehpur"}
]
res = coll.insert_many(DATA)
print("DATA inserted....")
print(res.inserted_ids)