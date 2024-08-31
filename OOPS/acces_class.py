class Person:
     name= "anomous"

     # def changeName(self,name):
     #      #Person.name=name
     #      self.__class__.name=name

     @classmethod
     def changeName(cls,name):
          cls.name=name

p1=Person()
p1.changeName("Harsh Agrawal")
print(p1.name)
print(Person.name)
