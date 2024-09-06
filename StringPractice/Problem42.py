import collections

ex='thequickbrownfoxjumpsoverthelazydog'
dt = {}
for char in ex:
     dt.update({char:0})
count=0
for key,value in dt.items():
     for i in ex:
          if(i==key):
               value+=1
               dt.update({key:value})

for char in sorted(dt,key=dt.get,reverse=True):
     if dt[char] > 1:
        # Print the character and its count.
        print('%s %d' % (char, dt[char])) 