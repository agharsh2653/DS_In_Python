a = (2,34, 53, 65, "keshav", "manvik", 45.0 )
print(type(a))
# a[1] = 12  tuples does not suport item assignment

my_tuple = (2,3,6,9,12,19,6)
count_6 = my_tuple.count(6)
print(count_6)

index_3 = my_tuple.index(3)
print(index_3)

tuple1 = (1,2,3)
tuple2 = (4,5,6)
concatenated = tuple1 + tuple2
print(concatenated)

print(9 in my_tuple)
print(4 in my_tuple)

#Slicing : Tuples supports slicing to create new tuple from a subset of original tuple
sliced = concatenated[2:5]
print(sliced)

#Unpacking : tuple can be unpacked into individual variables
a, b, c = tuple1
print(a, b, c)

