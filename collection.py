from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client['mydb']

collection = db["example"]
print("collection created")