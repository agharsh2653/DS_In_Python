import mysql.connector

mydb = mysql.connector.connect(host="localhost", user = "root", password ="Mahadev07ji$",database="testdb")

my_cursor = mydb.cursor()
upQuery = "update employee set address='Delhi' where em_name = 'Anita' "
orderQuery = "select * from employee order by em_name asc"
query = "select * from employee"
deleteQuery = "delete from employee where em_name like 'An%'"
dropTable = "drop table if exists employee"
# my_cursor.execute(deleteQuery)
# my_cursor.execute(query)
my_cursor.execute(dropTable)

# myResult = my_cursor.fetchall()
# for row in myResult:
#      print(row)

mydb.commit()
mydb.close()