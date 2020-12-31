import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="12345",database="mydatabase")

mycursor = mydb.cursor()

sql = "INSERT INTO customers(name,address)VALUES(%s,%s)"
val = ("Satish","sangli")

mycursor.execute(sql,val)

mydb.commit()

# Important!: Notice the statement: mydb.commit(). 
# It is required to make the changes, otherwise no changes are made to the table
print(mycursor.rowcount,"row inserted..")