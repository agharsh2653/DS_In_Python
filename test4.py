li = [1,2,34,33,5]

min =li[0]
max =li[0]
for i in range(0,len(li)):
     if(min>li[i]):
          min=li[i]
     if(max<li[i]):
          max=li[i]

print(min)
print(max)
