# Python lists are containers to store a set of values of any data type.
# List is ordered collection of elements.
# they are mutable, means the values can be altered after creation.
# These are similar to arrays in c, cpp.

l1 =  [1,3,5,7,9]  # create a list.
print(l1)

if 3 in l1:
    print("True"); # will return true since 3 in declared as an integer in the if condition.
else:
    print("False"); # is 3 is not present in the list will return as false 

if "3" in l1:
    print("3 is present.");
else:
    print("Not present, since it is a string datatype."); # will print false since the list contains 3 but in integer form, in if condition the 3 is declared as a string "3".

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

listx = ['z','w','t','a','e'];
print(listx);

# .sort() : sorts the element  of the list from ascending order
list1.sort() # will return the list in an ascending order of the integers given in the list.
print("This is a sorted list : ",list1)
listx.sort(); # will return the list in an alphabetical order of the string in the list.
print("This is a sorted list : ",listx);

# .reverse() : reverses the list.
list1.reverse()
print(list1)

# .append(element) : adds the element at the end of the list.
print(list1)
list1.append(687)
print(list1)

# .insert(index no. , element) : inserts the element at the mentioned index no.
list1.insert(0,23)   # will insert 23 at index no. 3
print(list1)

# .count(element) : will count the occurence of the element in the list.
print("Occurence of 203 in the list :",list1.count(203));

# p.extend(q) : will add the elements of q list to the end of p list.
p = [1,2,3,4,5];
q = [6,7,8,9,10];
p.extend(q);
print(p);

# concatenation of list : joining the two or more than two list.
s = ["hello", "world"];
t = ["!", "This", "is", "Python"];
k = s+t;
print(k);

# .pop(index no.) : will delete the element of the mentioned idex no.
list1.pop(3)  # this will delete the element present at index no. 3
print(list1)

# .remove(element) : will remove the element from the list. The only difference betn pop and remove is that pop() uses the index no. to delete the element and remove() uses the element itself to remove.
list1.remove(2910)   # 2910 will be removed from the list.
print(list1)

# .clear() : removes all the elements from the list.
print(list1)
# list1.clear()  # will delete all the elements of the list and empty list will be printed.
print(list1)

# .copy() : 
list1.copy()
print("this is the copy of the list  : ",list1)

# List Comprehension : Creating a list on the go. means, creating a new list 
# from other iterables like lists, tuples, dictioneries, sets, arrays and strings.

# following snippet shows how a list can be created using for and range() function. 
z = [i for i in range(21)]; # this will return a list consisting of values ranging from 0 to 20.
print(z);

# The code below will print the table of two.
# The range is given from 1 - 11, since 11 will be excluded, it will print only till 10.
# The i will iterate over the range from 1 to 11 and will be multiplied by 2 each time.
# The multiplication output will be in the form of list.
y = [i*2 for i in range(1,11)];
print(y);

# Multiplying each number with itself over the range of i:
x = [i*i for i in range(1,11)];
print(x); # will print the multiplication of each number with itself.

# Create a list having even numbers from 0 - 40:
m = [i for i in range (1,41) if (i % 2 == 0)];
print(m);
print(len(m));


