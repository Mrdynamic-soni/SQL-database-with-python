import sqlite3

conn = sqlite3.connect("test.db")
curs = conn.cursor()
print("database openend succesfully")

data = "select * from database"
res = curs.execute(data)
print(res.fetchall())