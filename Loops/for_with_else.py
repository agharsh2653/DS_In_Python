li = [1, 83, 34, 90]

for i in li:
    print(i)

else:
     print("Done") 
     print()


for i in range(1,100):
     if(i==11):
          break #Exit the loop right now
     print(i)

print()
for i in range(1,100):
     if(i%2==0):
          continue #Skip the iteration
     print(i)
