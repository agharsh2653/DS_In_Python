st1="restart"
ch = st1[0]
for i in range(1,len(st1)):
     if(st1[0]==st1[i]):
          ch+=st1[i].replace(st1[0],"$")
     else:
          ch+=st1[i]

print(ch)
