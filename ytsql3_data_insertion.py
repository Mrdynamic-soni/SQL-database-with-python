import sqlite3

conn = sqlite3.connect("test.db")
print("database openend succesfully")

data = "insert into database(sensor_name,temperature,humidity) values('dht11',23.8,448) "
conn.execute(data)


conn.commit()
