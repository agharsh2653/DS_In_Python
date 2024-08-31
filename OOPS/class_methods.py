class Employee:
     a=1
     @classmethod
     def show(cls):
          print(f"The class attribute of a is {cls.a}")

     @property
     def name(self):
          return f"{self.fname} {self.lname}"
     
     @name.setter
     def name(self,value):
          self.fname=value.split(" ")[0]
          self.lname=value.split(" ")[1]

e=Employee()
e.a=21
print(e.a)

e.name = "Harsh Agrawal"
print(e.fname,e.lname)
e.show()