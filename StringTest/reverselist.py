#WAPP to reverse any two list and then join them in a new list
l1 = [1,2,3,"harsh","manvik"]
l2 = [4,5,6,"Lekh","keshav"]

reversel1 = l1[::-1]
reversel2 = l2[::-1]
joinlist = reversel1+reversel2
print(joinlist)