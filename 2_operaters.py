# to comment use shortcut ctrl+/


#Arithematic operaters4
a=22
b=11
print("the addition of a+b = ",a+b)
print("float format",a//b)   # '//' prints the  o/p of the integers in float format 
print ("no float format",a/b)  #'/' prints o/p of the integers as in integer format
print("The square of 22 is ",a**2)   #'**' prints the exponential value.
print(a*b);
#Assignment operaters
a *= 4
print(a)
b -= 10
print(b)
a += 2
print(a)
b /= 10
print(b)


#Comparison operaters
x = (2>3)    #less than or greater than operator.
print("the value is ", x)

y = 1
z = 4
c = 0
m = (1!=4)   #not equal to operator.
n = (0==4)
print("the value is ", m,n)  

 
#logical operaters

# Create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers.
num1 = int(input("Enter first number :"));
num2 = float(input("Enter second number :"));
add = num1 + num2;
print(num1,"+",num2,"=", add);
sub = num1 - num2;
print(num1,"-",num2,"=", sub);
mul = num1 * num2;
print(num1,"*",num2,"=", mul);
div = num1 / num2; #will print o/p in integer format.
print(num1,"/",num2,"=", div);
div1 = num1 // num2; #will print o/p in float format.
print(num1,"//",num2,"=", div1);
rem = num1 % num2;
print(num1,"%",num2,"=", rem);
pow = num1 ** num2;
print(num1,"**",num2,"=", pow);
