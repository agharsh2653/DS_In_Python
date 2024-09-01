class Employee:
     company = "ITC"
     name = "Harsh"
     def show(self):
          print(f"The name of the employee is {self.name} and the name of company is {self.company}")
     
class Coder:
     language = "Python"
     def printLanguage(self):
          print(f"Out of all the languages here is your language: {self.language}")


class Programmer(Employee,Coder):
     company="ITC Infotech"
     #language ="Java"
     def showLanguage(self):
          print(f"The name of the employee is {self.name} and he is good with {self.language} language")

a=Employee()
b=Programmer()
b.show()
b.showLanguage()
b.printLanguage()
print(a.company,b.company)