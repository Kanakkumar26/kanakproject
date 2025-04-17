import mysql.connector 

db = mysql.connector.connect(host="localhost",user="root",password="",database="mysql")

print(db)

cr = db.cursor()
data = cr.execute('show databases')
# print(data)
# db.commit()
print(cr.fetchall())


db.close()