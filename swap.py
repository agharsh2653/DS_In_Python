a, b, c, d= 10, 20, 30, 40
'''c=a
a=b
b=c'''
# a=a+b
# b=a-b
# a=a-b
#right swap
# a=a+b+c
# b=a-b-c
# c=a-b-c
# a=a-b-c
#left swap
# c=a+b+c
# b=c-a-b
# a=c-a-b
# c=c-a-b
# print(a, b, c)

#left swap
# d=a+b+c+d
# c=d-a-b-c
# b=d-a-b-c
# a=d-a-b-c
# d=d-a-b-c
# print(a, b, c, d)

#swap right
a=a+b+c+d
b=a-b-c-d
c=a-b-c-d
d=a-b-c-d
a=a-b-c-d
print(a, b, c, d)