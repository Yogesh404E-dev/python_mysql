# import mysql  lib .connector 
import mysql.connector

#create mysql object using creaditional of local host 
mydb = mysql.connector.connect(host="localhost",user="root",password="12345")
#print the connection object 
print(mydb)
