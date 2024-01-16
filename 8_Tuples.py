# A tuple is an immutable datatype in python. No changes can be made in a tuple once created.
# There is no direct way to alter the values of already declared tuple.
# To add, remove or alter the elements in a tuple, convert it to a list first, update the list and then convert it to tuple again.
t1 = (3,6,8,4,0)
print("This is a tuple : ",t1)

if 5 in t1:
    print("true");
else:
    print("false");

# If the tuple is tried to be updated by changing its values it throws an error, since no values can be altered in the tuple.
# t1[0]=0
# print(t1)   # it does not support item assignment.

# tuple with only one element : 
t2 = (2,)  # always add comma after the element, otherwise adding only e element will show an error.
print(t2)

# updating a tuple by converting it into a list :
tup = ("orange","banana","grapes");
print(type(tup));
convert = list(tup); # converting the tuple into list
print(type(convert));
convert.append("watermelon"); # adding the new element into the list.
print(convert);
tup = tuple(convert); # converting the updated list into tuple again.
print(tup);

                            #  OR   

# by concatenating two tuples, we can update the tuple.
tup1 = ("orange","banana","grapes");
tup2 = ("watermelon",);
t2 = tup1 + tup2;
print("by concatenating 2 tuples : ",t2);


# Methods in tuple
# .count() : counts the occurence of that particular element.
t1 = (3,6,8,4,4)
print(t1.count(0))
print(t1.count(4))

# .index() : Will give the index no. of that element.
# print(t1.index(2))   # when the element is not there in the list it will throw an error as 'tuple not in the list' as in this case.
print(t1.index(4))

