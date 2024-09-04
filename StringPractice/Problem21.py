def convet_upper(up):
     count=0
     for ch in up[:4]:
          if(ch >= 'A' and ch <= 'Z'):
               count+=1
     if(count>=2):
          return up.upper()
     
print(convet_upper("W3Resource"))