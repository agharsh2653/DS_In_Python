class Account:
     def __init__(self,acc_no,acc_pass):
          self.acc_no = acc_no
          self.__acc_pass = acc_pass

     def reset(self):
          print(self.__acc_pass)
          self.__hello()

     def __hello(self):
          print("Hello World")

acc1=Account("12345","abcde")
print(acc1.acc_no)
 
#here we define acc_pass as private acces modifier threw __
#print(acc1.__acc_pass)

print(acc1.reset())
#print(acc1.__hello()) #AttributeError: 'Account' object has no attribute '__hello'