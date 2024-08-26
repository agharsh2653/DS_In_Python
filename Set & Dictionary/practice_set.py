# Hindi_dict = {
#      "murga":"cock",
#      "hati":"elephant",
#      "dukh":"sadness",
#      "khusii":"happiness"
# }
# word = input("Enter the word")
# print(Hindi_dict[word]) #p1

# s = set()
# s1 = int(input("Enter the  number "))
# s.update(s1)
# s2 = int(input("Enter the  number "))
# s.update(s2)
# s3 = int(input("Enter the  number "))
# s.update(s3)
# s4 = int(input("Enter the  number "))
# s.update(s4)
# s5 = int(input("Enter the  number "))
# s.update(s5)
# s6 = int(input("Enter the  number "))
# s.update(s6)
# s7 = int(input("Enter the  number "))
# s.update(s7)
# s8 = int(input("Enter the  number "))
# s.update(s8)
# print(s) #p2

# s.update(18)
# s.update("18")
# print(s)#p3

# h = set()
# h.add(20)
# h.add(20.0)
# h.add("20")
# print(h)
# print(len(h)) #p4

# i = {}
# print(type(i))#p5

friend = {}

name = input("Enter the name ")
lang = input("Enter the language ")
friend.update({name:lang})
name = input("Enter the name ")
lang = input("Enter the language ")
friend.update({name:lang})
name = input("Enter the name ")
lang = input("Enter the language ")
friend.update({name:lang})
name = input("Enter the name ")
lang = input("Enter the language ")
friend.update({name:lang})
print(friend) #p6
# in this problem we use update in which when we enter same key value as name then dict update their key value
# p7 The value entered later will be updated
# p8 Nothing will heppen simply add in dictionary (when we add same value)

un = {8, 7, 16,"harry", [1,2]}
# p9 in this we could not change the list element insit the set 
# but we can use tuple to update it 
