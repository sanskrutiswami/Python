# A tuple is an immutable datatype in python. No changes can be made in a tuple.
t1 = (3,6,8,4,0)
print("This is a tuple : ",t1)

# If the tuple is tried to be updated by changing its values it throws an error, since no values can be altered in the tuple.
# t1[0]=0
# print(t1)   # it does not support item assignment.

# tuple with only one element : 
t2 = (2,)      # always add comma after the element, otherwise adding only e element will show an error.
print(t2)

# Methods in tuple
# .count() : counts the occurence of that particular element.
t1 = (3,6,8,4,4)
print(t1.count(0))
print(t1.count(4))

# .index() : Will give the index no. of that element.
# print(t1.index(2))   # when the element is not there in the list it will throw an error as 'tuple not in the list' as in this case.
print(t1.index(4))
