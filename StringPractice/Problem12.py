sentence = "Hello my is Hello harsh my friend is"

word= sentence.split(" ")
dict = {}
for i in word:
     dict.update({i:0})

for key,value in dict.items():
     for i in word:
          if(i==key):
               value+=1
               dict.update({key:value})
print(dict)