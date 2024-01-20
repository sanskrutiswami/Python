# Sets in Python are unordered collection of data.
# Stores multiple items in a single variable.
# Sets are immutable. Meaning once created it cannot be updated or altered.
# Values are stored in between {} brackets and seperated by commas.
# They do not contain duplicate items.

set0 = { };
print(type(set0)); # will print - <class 'dict'>
# The dataype of an empty set0 is Dictionary.
# Since the dictionary also uses curly brackets, interpretor will interpret it as a dictionary.

# To print an empty set :
# Use keyword set followed by (). This is an empty set.
set_empty = set();
print(type(set_empty)); # will print - <class 'set'>

set1 = {1,2,3,4,5,6,6,6,3.14};
print(f"This is a set : {type(set1),set1}");
print(f"This is a set : {type(set1),set1}");
# in set1, 6 is repeated 3 times, but it will print only once.

set2 = {"hello", "this", "is", "year", 2024};
print(f"This is another set : {type(set2),set2}");
# the above code will genrate a set but the elements will be not in order as declared in the set.
# the order will change randomly everytime you will call the variable set2.

# Another way of printing the values in set is by using for loop :
set3 = {"hi","this", "is", "Python", 3.11};
for value in set3:
    print(value);
# this will print the values randomly, and each value will be on new line.


# Methods in Sets :
# Sets in Python is the same concept as in Mathematics.
# Hence, sets will have methods like union, intersection, etc.

# .union() : when used this method, gives the output of combination of two or more sets
# if both sets share common values, those will be not repeated.
s1 = {1,2,3,4,6,8};
s2 = {1,3,4,5,7,9};
uni = s1.union(s2);
print("This is Union s1 U s2 = ",uni);

# .intersection() : this method will only print the values which are present in both of the sets.
s3 = {1,2,3,4};
s4 = {2,4,6,8};
inter = s3.intersection(s4);
print("This is an intersection = ",inter);

# _update() : even though sets are immutable, they can be altered using update method.
# More values can be added using this method.
s3.update(s4);
print(s3);
s4.update(s3);
print(s4);

# isdisjoint() : this method checks if the values of the given set are present in another set.
# It will return false if items are present and true if not present.
print(s3.isdisjoint(s4)); # will return false since s4 values are present in s3 set.
s5 = {7,5,9,0};
print(s5.isdisjoint(s4));# will return true since there are no common values in both sets.

#  .superset() & .subset() : The set which contains all the values present in another set is the superset.
# the set which is a part of the superset, that means the set which contains the values which are also present in superset along with other values.
# These both methods will return as True or False depending upon whether they are superset or subset to each other.
s6 = {1,2,3,4,5,6,7,8,9};  # this is a superset since s7 set values are present in this set.
s7 = {2,4,6,8}; # this is the subset of s6 since s6 contains all the values present in s7.
print("s6 is superset of s7 : ", s6.issuperset(s7)); # will return true.
print("s7 is the subset of s6 : ", s7.issubset(s6)); # will return true.

# add() : Unlike update method, the add() method adds only one value to the set.
fruits = {"apple", "banana", "orange"};
fruits.add("guava");
print(fruits); 
# !!!note : add() cannot be used in print() statement,if used it will return as None. Has to declared separately!!!

# remove() OR discared() : removes or discards the specified value from the set.
# The difference between both is that, if we try to remove() an element which is not present in the set, it will throw an error,
# but if we discard() an element which is not present in the set it will not throw an error.
countries = {"India","Italy","Sri Lanka","USA"};
countries.remove("Italy");
print(countries);
countries.discard("India");
print(countries);
countries.discard("Russia"); # will print the set as it is and will not throw an error.
print(countries);
# countries.remove("Russia"); # will throw an error : KeyError: 'Russia'
# print(countries);
# !!!note : remove() pr discard() cannot be used in print() statement,if used it will return as None. Has to declared separately!!!

# pop() : This method will randomly pop or print an element from the given set.
veggies = {"spinach", "tomato", "broccoli", "cabbage", "beans"};
p = veggies.pop(); # will pop a random element from the set, and store it in variable p.
print(p);

# del() : deletes the whole set.
car = {"BMW", "Toyota", "Jaguar"};
print(car); # will print the set
del(car); # will delete the whole set.
# print(car); # will throw an error as undefined, since the set is deleted.

# Using if-else condition to check if the item is present in the list or not:
# Just like other datatypes like lists and dicts, we can use conditional statement if else to check whether the element is present in the set or not.
languages = ("Python","C++","Java","ruby");
if "javascript" in languages :
    print("Not present");
else:
    print(languages);




