a="abc"
b="xyz"
result=""
for i in range(0,2):
    result+=b[i]
result+=a[2:]+" "
for i in range(0,2):
    result+=a[i]
result+=b[2:]
print(result)