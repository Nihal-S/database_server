import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
# query = "CREATE TABLE sample(title varchar(20),data varchar(200))"
# query = "INSERT INTO sample(title,data) VALUES('NIHAL','lives in bangalore')"
query = "SELECT * FROM sample"
c.execute(query)
rows = c.fetchall()
for i in rows:
    print(i)
conn.commit()
conn.close()