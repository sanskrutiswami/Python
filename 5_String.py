# Strings are immutable datatypes.
# single quote, double quote and triple single quote strings : 

str1 = "Sanskruti's" # use double quotes if the string contains a single quote.
str2 = '"hello there"' # use single quote or three times single quote if the string contains double quote.
str3 = '''Sanskruti's
           and 
            Sanskruti's''' # also by using triple single quotes and tab key one can put spaces and print the string on new line without getting indentation error
print(str1)
print(str2)
print(str3)

# Operations on String:
# String Slicing : String slicing means to slice the string by using the idex no.
string1 = "Hello there! Have a good day."
print(len(string1))
print(string1[3])
print(string1[6])
print(string1[0:9]) # here the whole string will be sliced from index no. 9 that means only the literals present form index 0 to 8 will be printed.
# the first indices is included while the last indice is excluded while printing the o/p
# similarly,
print(string1[5:11])
# Negative indices can be also used to access the literals
print("negative indices",string1[0:-3])
print("negative indices",string1[-3:-1])
x="harry"
print(x[-4:-2],x)
# SKip value prints the string while skipping the literals in the string.
print("s",string1[0::3]) # here every 3rd letter will be skipped.
print("hello",string1[:]); # will print the whole string.
# String concatenation : Joins two or multiple strings together
a = "This is"
b =  " VS code."
print(a+b)
#     OR
c = a+b
print(c)


# String functions :
# index : 
name = "sanskruti";
print(name[3]);

# printing characters from the string using for loop : 
for character in name:
    print(character); #this prints every character from the string one by one.

# len() : Determines the length of the string.
u = "this is Python Programming."
print("The length of this string is ",len(u))

# .endswith("args") : 
print(u.endswith(u)) # will return a True value because the string ends with the value of u.
print(u.endswith("is")) # will return a false value because the string does not end at is.
print(u.endswith("ing.", 0 , 27))

#  .count() : Counts the no. of occurances of a character or a word in the string.
print(u.count("t"))
print(u.count("i"))
print(u.count("q"))
print(u.count("This"))
print(u.count("this"))   # will return as 0 due to case-sensitivity

# .capitalize() : As the name suggests, it capitilises the first Character of  the string.
print(u.capitalize())


# .find("args") : This finds the particular character or word and its index no.
print(u.find("is"))
print(u.find("y"))

# .replace(old word, new word) : Replaces the current word with new word in the entire string.
arr = "sansSanskrutiSwami";
print(arr.replace("sans","sanskruti"));


# .upper() : gives the capitilized o/p of the string.
name = "Python 3";
print(name.upper());  # will capitalize the whole string.

# .lower() : prints the string in lowercase form.
lower = "python 3";
print(name.lower());

# .rstrip() : removes any trailing characters.
trail = "Welcome to Python 3 !!!!";
print(trail.rstrip("!"));

# .split() : spilts the string in form of list.
order = "Mango Banana Orange Kiwi Pineapple";
print(order.split(" "));
print(order.find("Mango"))
# print(order.index("pear"))

# .isalanum() :
num = "hellot here 123456789";
print(num.isalnum()); # will return false due to spaces.

num1 = "hellothere123456789";
print(num.isalnum()); # will return false due to spaces.




 














 





