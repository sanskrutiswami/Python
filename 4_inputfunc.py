# This function takes input from the user.
# e = input(" Enter your Id no. ")
# print (type(e))

#  code to print the square of an integer taken from input user.
t = input("Enter the number for to determine its square : ")
t = int(t) # If input parameter is taken to be an integer it is necessary to typecast the input func which is i string form.
print("The square of ",t,":",t**2)


# code to print whether the number is even or odd taken from the user.
e = int(input("Please enter the number of your choice :  "))
if e % 2 == 0 :
    {
        print(e," is an even number.")
    }
else :
    {
        print(e," is an odd no.")
    }


# code for printing the multiplication table of the no. taken from the user.
i = int(input("Enter the number : "))
print("The multiplication table of ",i,"is : ")
for l in range(1,11):
    print(i,"x",l,"=",i*l)


# 









