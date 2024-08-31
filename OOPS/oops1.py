class Employee:
     language="py" #This is a class attributes
     salary=120000

harsh = Employee()
harsh.name = "Harsh Kumar Agrawal" #This is a object attributes
print(harsh.name,harsh.language,harsh.salary)

koushal = Employee()
koushal.name = "koushal Kumar Agrawal"
print(koushal.name,koushal.language,koushal.salary)

#Here name is object attribute and salary and language are class
#attributes as they directly belong to the class