# Dictionary is the collection of keyvalue pairs.
#  In Python 3.7 onwards the dictionary datatype became ordered, before that they were unordere just like sets.

dict1 = {"int" : "integer value", "char" : "character value", "vsccode" : "visualstudiocode",
"numbers": "1,2,3,4,5,6,7,8,9,0" , 'dict2' : {'greetings':'hello there!'}}
print(dict1['int'])
print(dict1['char'])
print(dict1['numbers'])
print(dict1['dict2']) # dictionary in another dictionary
print(dict1['dict2'][ 'greetings'])
print(dict1.keys()); # wil give all the keys at once.
print(dict1.values()); # will give all the values at once.

# empty dictionary :
empty = {};
print(type(empty),empty);

# Iteration of the dictionary using for loop to print the key-value pairs one by one :
print("This is a dictionary : ");
for x in dict1 :
    print(dict1[x]);

# Accessing the key value pairs : will print the key-value pairs.
print(dict1.items());
for i, value in dict1.items():
    print(f"The value of the corresponding key {i} is {dict1[i]}");



# Methods in Dictionary :

# update() : used to update the dictionary, this works similar as update in sets.
# This method will add the key-value pairs of one dictionary to another dict.
d1 = {"greetings" : "hello", "name" : "Sanskruti", "language" : "python"};
d2 = {"editor" : "Vscode", "version" : 3.11};
d1.update(d2);
print(d1);

# pop() : takes the required key as an argument which will be removed along its corresponding value from the dict.
pp = {"greetings" : "hello", "name" : "Sanskruti", "language" : "python"};
pp.pop("name");
print(pp);

# popitem() : removes the last key-value pair from the dict.
d3 = {"greetings" : "hello", "name" : "Sanskruti", "language" : "python", "editor" : "Vscode", "version" : 3.11};
d3.popitem();
print(d3); # here the last key-value pair i.e. version : 3.11 will be removed.

# clear() : clears the whole dictionary and will return as an empty dict.
d4 =  {"greetings" : "hello", "name" : "Sanskruti", "language" : "python", "editor" : "Vscode", "version" : 3.11};
d4.clear();
print(d4); # will print as an empty dict - {}
# the cleared or empty d4 dict can be once again assigned new key-value pairs.
d4 = {"greetings" : "hello world"};
print (d4);

# del[] :  deletes the whole ditionary if no argument is passed in this method.
# But if an argument, i.e. a key is passed, it will delete only the specified key-value pair from the dict.
d5 = {"greetings" : "hello", "name" : "Sanskruti", "language" : "python", "editor" : "Vscode", "version" : 3.11}
del d5["greetings"];
print(d5);
del(d5);
# print(d5); will throw an error as not defined, since it has been deleted.





