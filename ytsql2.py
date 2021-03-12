import sqlite3

conn = sqlite3.connect("test.db")
print("database created")

data = "create table database(sensor_name text,temperature float,humidity float)"
conn.execute(data)
print("table created")