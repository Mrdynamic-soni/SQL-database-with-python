from pymongo import MongoClient
from pymongo.errors import BulkWriteError

#Creating a pymongo client
client = MongoClient('localhost', 27017)

#Getting the database instance
db = client['mydatabase']

#Creating a collection
coll = db['example']

#Inserting document into a collection
data = [
   {"_id": "101", "name": "Ram", "age": "26", "city": "Hyderabad"},
   {"_id": "102", "name": "Rahim", "age": "27", "city": "Bangalore"},
   {"_id": "103", "name": "Robert", "age": "28", "city": "Mumbai"}
]
res = coll.insert_many(data)
print("Data inserted ......")
print(res.inserted_ids)

#Retrieving the first record using the find_one() method
print("First record of the collection: ")
print(coll.find_one())

#Retrieving a record with is 103 using the find_one() method
print("Record whose id is 103: ")
print(coll.find_one({"_id": "103"}))

for doc1 in coll.find():
    print(doc1)

for doc2 in coll.find({"age":{"$gt":"26"}}):
 print(doc2)
