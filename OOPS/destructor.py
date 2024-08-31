class Student:
     def __init__(self,name):
          self.name=name

s=Student("Harsh")
print(s.name)
del s.name
print(s)
print(s.name)
