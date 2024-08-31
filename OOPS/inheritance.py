class Employee:
     company = "ITC"
     name = "Harsh"
     def show(self):
          print(f"The name of the employee is {self.name} and the name of company is {self.company}")
     
# class Programmer:
#      company = "ITC Infotech"
#      def show(self):
#           print(f"The name of the employee is {self.name} and the name of company is {self.company}")

#      def showLanguage(self):
#           language ="Java"
#           print(f"The name of the employee is {self.name} and he is good with {self.language} language")

class Programmer(Employee):
     company="ITC Infotech"
     language ="Java"
     def showLanguage(self):
          print(f"The name of the employee is {self.name} and he is good with {self.language} language")

a=Employee()
b=Programmer()
b.show()
b.showLanguage()
print(a.company,b.company)