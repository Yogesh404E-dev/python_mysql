import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="12345",database="mydatabase")

mycusor = mydb.cursor()

mycusor.execute("SELECT * FROM customers")

mysqlresult = mycusor.fetchall()

for x in mysqlresult:
    print(x)