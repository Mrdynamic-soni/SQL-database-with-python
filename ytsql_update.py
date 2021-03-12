import sqlite3

conn = sqlite3.connect("test.db")
print("database openend succesfully")

data = "update database set humidity = 46 where temperature = 2"
conn.execute(data)

conn.commit()

data = "select * from database"
res = conn.execute(data)
print(res.fetchall())
print("\n")
