import sqlite3

conn = sqlite3.connect('identity.db')
c = conn.cursor()
# query = "CREATE TABLE sample(title varchar(20),data varchar(200))"
# query = "INSERT INTO sample(title,data) VALUES('NIHAL','lives in bangalore')"
# query = "SELECT * FROM sample"
query = "CREATE TABLE aadhar(aadhar_no varchar(12),name_of_person VARCHAR(50),mobile_number varchar(20),adress VARCHAR(50));"
c.execute(query)

rows = c.fetchall()
for i in rows:
    print(i)
conn.commit()
conn.close()