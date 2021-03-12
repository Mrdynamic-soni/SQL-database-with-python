from pymongo import MongoClient

#Creating a pymongo client
client = MongoClient('localhost', 27017)

#Getting the database instance
db = client['mydatabase']

#Creating a collection
coll = db['example']

#Inserting document into a collection
data = [
   {"_id": "!", "name": "Ram", "age": "26", "city": "Hyderabad"},
   {"_id": "!!", "name": "Rahim", "age": "27", "city": "Bangalore"},
   {"_id": "!!!", "name": "Robert", "age": "28", "city": "Mumbai"}
]
res = coll.insert_many(data)
print("Data inserted ......")
print(res.inserted_ids)

#Retrieving the first record using the find_one() method
print("First record of the collection: ")
print(coll.find_one())

#Retrieving a record with is 103 using the find_one() method
print("Record whose id is 103: ")
print(coll.find_one({"_id": "!!!"}))