class Employee:
     a=2
     def __init__(self):
          print("Constructer of employee")

class Programmer(Employee):
     b=5
     def __init__(self):
          print("Constructer of Programmer")

class Coder(Programmer):
     c=7
     def __init__(self):
          print("Constructer of coder")

o=Employee()
print(o.a) # it could not access b and c
p=Programmer()
print(p.a,p.b) # it could not accesss c

c=Coder()
print(c.a,c.b,c.c)
