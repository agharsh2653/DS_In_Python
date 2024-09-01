from random import randint
class Demo:
     a=5

o=Demo()
print(o.a)
o.a=0
print(o.a)
print(Demo.a) #it does not change in instance of a class

class Train:
     # def __init__(self,trainNo):
     #      self.trainNo = trainNo
     def __init__(slf,trainNo):
          slf.trainNo = trainNo
     def book(harsh,fro,to):
          print(f"Ticket is booked in train no: {harsh.trainNo} from {fro} to {to}")

     def getStatus(self):
          print(f"Train no is {self.trainNo} is running on time")

     def getFare(self,  fro,to):
          print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,6666)}")

t = Train(12195)
#t.trainNo = 12195
t.book("Bharatpur","Jaipur")
t.getStatus()
t.getFare("Bharatpur","Jaipur")