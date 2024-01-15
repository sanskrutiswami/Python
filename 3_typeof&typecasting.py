# typeof function 
a = "hello world"
b = 456
c = 45.06
d = True
e = 230.49574859
print(a)
print(b) 
#printing the type of the variables
print( a,type(a))
print( b,type(b))
print( c,type(c))
print( d,type(d))
print( e,type(e)) ;

# type casting
# In type casting one can convert the data type of the variable into anothe.
# An interger can be convterted into a string and vice versa.
p = "45"
print("the dataype is ",type(p))
p = int(p)
print ("The datatype is ",type(p))
print(p+5) 

q = "3876290"
print(" the datatype is ",type(q))
print(q)
q = int(q)     # typecasting the string into int datatype.
print(q)
print ( "the datatype is ",type(q))

# If the string literal is the combination of numbers and characters then it will not be able to type cast,i.e it will not convert from string to int.
#example :
# r = "308503tyuer"
# print(type(r))
# r = int(r)
# print(type(r))    #it will show an error : invalied literal for int()

# IMPLICIT TYPECASTING :
# In python, datatypes have higher and lower orders. According to the level of
# one dataype in converted into other by the python interpretor itself. This
# is called as implicit typecasting in python. Python converts a smaller datatype
# to a higher order data type to prevent data loss.
num1 = 4;
num2 = 2.2;
print(num1,type(num1));
print(num2,type(num2));
print(num1+num2,type(num1+num2)); #here the sum of int and float gets converted into float by default.


      