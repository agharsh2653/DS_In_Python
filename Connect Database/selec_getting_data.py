import mysql.connector

mydb = mysql.connector.connect(host="localhost", user = "root", password ="Mahadev07ji$",database="testdb")

my_cursor = mydb.cursor()
query = "select em_name from employee where emp_id = 4"
my_cursor.execute(query)
myResult = my_cursor.fetchall()
for row in myResult:
     print(row)

mydb.close()
