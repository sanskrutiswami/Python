# In Python a function can call other functions. A function
# can call itself as well. Such fuctions are called as recursive fuctions.

# Example of calculating a factorial :
def factorial (n):
    if (n == 1 or n == 0):
        return 1
    else :
        return (n + factorial(n - 1));
# Driver code :
x = int(input("Enter a number : ")); 
if (x <= 0):
    print("Enter a positive value.");
else:
    for i in range(x):
        print(factorial(i)); # This will print the factorial from 1 upto the number the user has enterd.
# if user enters 10 as an input, then first 10 factorials will be printed.
# print(f"The factorial of {n} is {factorial(n)}");



# Example of creating a Fibonacci sequeunce.
# mathematical expression is f(n) = f(n-1) + f(n+1)
# that means the current number is the sum of previous two numbers.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 33.....and so on.
# Now take an input value from the user and generate the sequence.
def Fibonacci (f):
    if (f == 1 ):
        return 1
    elif (f == 0):
        return 0
    else:
        return(Fibonacci(f-1) + Fibonacci(f-2));
# Driver code :
userinput = int(input("Enter a number : "));
if (userinput<=0):
    print("enter a positive value.");
else:
    for i in range(userinput):
        print(Fibonacci(i));

# print(Fibonacci(0));
# print(Fibonacci(1));
# print(Fibonacci(2));
# print(Fibonacci(3));
# print(Fibonacci(4));
# print(Fibonacci(5));
# print(Fibonacci(6));



