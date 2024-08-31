class Employee:
     language="Python" #This is a class attributes
     salary=120000

     def __init__(self,name,salary,language): #dunder method call when creating a new object
          self.name = name
          self.salary = salary
          self.language = language
          print("I am creating an object")

     def getInfo(self):
          print(f"The language is {self.language}. The salary is {self.salary}")
     
     @staticmethod 
     def great():
          print("Good Morning")

harsh = Employee("Harsh", 55000,"Java")
#harsh.name = "Harsh Kumar Agrawal" #This is an instance

print(harsh.name,harsh.language,harsh.salary)


