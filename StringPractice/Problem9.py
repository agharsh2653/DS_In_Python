word = "hello word"
n = int(input("enter the index: "))
ch = ""
newStr =""
for i in range(0,len(word)):
     if n==i:
          continue
     else:
          ch+=word[i]
     
     if i%2!=0:
          continue
     else:
          newStr+=word[i]


print("P9 To remove the nth index character from a nonempty string",ch)
print("P11 To remove characters that have odd index values in a given string",newStr)