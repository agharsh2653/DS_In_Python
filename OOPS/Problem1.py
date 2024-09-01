class Programmerr:
     company = "Microsoft"
     def __init__(self,name,salary,pin):
          self.name=name
          self.salary = salary
          self.pin = pin

p = Programmerr("Harsh", 120000,321001)
print(p.name,p.salary,p.pin,p.company)
r = Programmerr("Yogesh", 120000,321001)
print(r.name,r.salary,r.pin,r.company)