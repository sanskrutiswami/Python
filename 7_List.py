# Python lists are containers to store a set of values of any data type.
# List is ordered collection of elements.
# These are similar to arrays in c, cpp.

l1 =  [1,3,5,7,9]  # create a list.
print(l1)

print(l1[4])  # the square brackets contains the index no. of the particular element of the list.
# The element can be accessed by using the index no.

# The values of the list can be also changed.
# Now as shown above the value on the 4 index is 9, lets change it to 33.
l1[4] = 33
print(l1)  # whole list will be printed along with the changed value.
print(l1[4])  # the changed value will be printed.

# List with different datatypes.
l2 = ['hello world', 493, 389.4, 3839203234, 'this is list']
print(l2)

# List slicing :
prg = ['python', 'swift', 'c++', 'java', 'sql', 'html', 'ruby', 'pascal']
print(prg[0:5]) #will print from index 0 to index 4. Last index mentioned will be always excluded and first will be included.
print("the reverse order of the list is : ",prg[::-1])  # prints the list in reverse order.
print(prg[2:7])
print(prg[-3:]) # negative indexing starts from the last element. this will print the last 3 elements of the list.

# List Methods : (vvimp)(mostly used)

list1 = [793,203,0,95,2910,44]
print(list1)

# .sort() : sorts the element of the list from ascending order
list1.sort()
print(list1)

# .reverse() : reverses the list.
list1.reverse()
print(list1)

# .append(element) : adds the element at the end of the list.
print(list1)
list1.append(687)
print(list1)

# .insert(index no. , element) : inserts the element at the mentioned index no.
list1.insert(3,23)   # will insert 23 at index no. 3
print(list1)

# .pop(index no.) : will delete the element of the mentioned idex no.
list1.pop(3)  # this will delete the element present at index no. 3
print(list1)

# .remove(element) : will remove the element from the list. The only difference betn pop and remove is that pop() uses the index no. to delete the element and remove() uses the element itself to remove.
list1.remove(2910)   # 2910 will be removed from the list.
print(list1)

# .clear() : removes all the elements from the list.
# print(list1)
# list1.clear()  # will delete all the elements of the list and empty list will be printed.
# print(list1)

# .copy() : 
list1.copy()
print("this is the copy of the list  : ",list1)





