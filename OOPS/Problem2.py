class Calculator:
     def __init__(self,n):
          self.n=n

     def square(self):
          print(f"The square is {self.n**2}")

     def cube(self):
          print(f"The cube is {self.n**3}")

     def squareRoot(self):
          print(f"The squareroot is {self.n**1/2}")

     @staticmethod
     def hello():
          print("Hello world")

a= Calculator(4)
a.square()
a.cube()
a.hello()
a.squareRoot()
