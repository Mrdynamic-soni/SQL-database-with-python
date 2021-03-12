from pymongo import MongoClient

#Creating a pymongo client
client = MongoClient("mongodb://localhost:27017/")

#Getting the database instance
db = client['mydb']
print("Database created........")

#Verification
print("List of databases after creating new one")
print(client.list_database_names())