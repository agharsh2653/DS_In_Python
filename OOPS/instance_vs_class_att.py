class Employee:
     language="py" #This is a class attributes
     salary=120000

     def getInfo(self):
          print(f"The language is {self.language}. The salary is {self.salary}")
     
     # def great(self):
     #      print("Good Morning")

     @staticmethod #this is define when no need of class atribute use then we define it
     def great():
          print("Good Morning")

harsh = Employee()
harsh.name = "Harsh Kumar Agrawal" #This is an instance attribute
harsh.language="javaScript"
#print(harsh.name,harsh.language,harsh.salary)
harsh.getInfo()
harsh.great()
#Employee.getInfo(harsh)

