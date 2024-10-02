import mysql.connector

connection = mysql.connector.connect(host="localhost", user = "root", password ="Mahadev07ji$",database="Pedestal")

if connection.is_connected():
    print("Connection succesfully")
else:
    print("Not connected") 

my_cursor = connection.cursor()
# query = "insert into employee(em_name, emp_id, department, address) values('Arun sharma', 2 , 'Python', 'Jaipur') "
# my_cursor.execute(query)
sqlformula = "insert into employee(em_name, emp_id, department, address) values (%s, %s, %s, %s)"
employee = [('Shidhika', 3, 'HR', 'Jaipur'),
            ('Anita', 4, 'Sales', 'Jaipur')]
my_cursor.executemany(sqlformula,employee)
# for db in my_cursor:
#     print(db)
connection.commit()
connection.close()