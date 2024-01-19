# f-strings are string formatting method for string datatypes in python.
# we can embedd python expression inside the string itself
# It is also called as literal string interpolation which is similar to template literal and string interpolation in Javascript.
# Prefix 'f' is used before any string for using f-string method.

name = "Sanskruti";
language = "Python";
print(f"Hello! My name is {name} and I am learning to code in {language}.")

list = ["orange","pineapple","watermelon", 555,"mango"];
print(f"Following is the list of fruits : {list}");

price = 22.999999;
print(f"The price of each fruit is {price:.2f}") # will print - The price of each fruit is 23.00
# by using 'variablename:.2f' the rounded off price of decimal digits will be printed.

print(f"This is how we use f-strings - Hello my name is {name}.")
# the above line will print name as "Sanskruti" since we have already defined it, if not define it will throw an error.
# But I have to show that how the f-string is written along with the curly barces, in that case double {{ }} curly braces are used : 
print(f"This is how we use f-strings - Hello my name is {{name}}.")
# this will print - This is how we use f-strings - Hello my name is {name}.

# we can also pass a python expression in f-string :
a = 2;
b = 5;
# in normal way we would write code in the following manner:
# print("Addition of a+b = ",a+b); wihich will give the same output.
# but to make it more convinient, it can be written in the following way using f-strings:
print(f"Addition of a + b = {a+b}"); # Addition of a + b = 7
print(f"Product of a*b = {a*b}"); # Product of a*b = 10

