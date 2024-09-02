ex="google.com"
dt = {}
for char in ex:
     dt.update({char:0})
count=0
for key,value in dt.items():
     for i in ex:
          if(i==key):
               value+=1
               dt.update({key:value})


print(dt)
