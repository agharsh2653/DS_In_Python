import mysql.connector

connection = mysql.connector.connect(host="localhost", user = "root", password ="",database="")

if connection.is_connected():
    print("Connection succesfully")
else:
    print("Not connected") 

my_cursor = connection.cursor()
query = "create table employee(em_name VARCHAR(40), emp_id int, department VARCHAR(40), address VARCHAR(40))"
my_cursor.execute("Create database Pedestal")
for db in my_cursor:
    print(db)
connection.commit()
connection.close()
