def average(a,b,c,d):
    avg = (a+b+c+d)/4;
    print(avg);
print("The average is : ");
average(a = 12, b = 34, c = 39, d = 44);
average(32, 99, 56, 0);

def null(a,b):
    pass

def greaternum(x,y):
    if(x>y):
        print(x," is greater than ",y);
    elif(x == y):
        print(x, "=",y);
    else:
        print(x," is less than ",y);
greaternum(x = 49, y = 20);
greaternum(64, 2);
greaternum(x = 0, y = 0);
greaternum(x = 23.5, y = 23);

def remainder(m, n):
    div = (m%n);
    if(m%n==0):
        print("The remainder is 0");
    else:
        print("The remainder is ",m%n);
print(remainder(m = 4, n = 3));
print(remainder(m = 22, n = 11));

def evenodd(x):
    if(x % 2 == 0):
        print(x," is an even number");
    else:
        print(x," is an odd number.");
evenodd(x=int(input("Enter a number : ")));


def average(*number):
    print(type(number));
    sum = 0;
    for i in number:
        sum = sum + i;
    print("Average of the given numbers is : ",sum/len(number));
average(2,4,6,4.3,7,34);



