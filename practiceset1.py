# Write a program to store seven fruits in a list entered by the user.
userip1 = input("Enter the name of fruit no. 1 : ")
userip2 = input("Enter the name of fruit no. 2 : ")
userip3 = input("Enter the name of fruit no. 3 : ")
userip4 = input("Enter the name of fruit no. 4 : ")
userip5 = input("Enter the name of fruit no. 5 : ")
userip6 = input("Enter the name of fruit no. 6 : ")
userip7 = input("Enter the name of fruit no. 7 : ")
l1 = [userip1,userip2,userip3,userip4,userip5,userip6,userip7]
print(l1)
print(l1[::-1])

# write a program to take input marks of 6 students and display them in the sorted manner.
std1 = int(input("Enter your marks : "))
std2 = int(input("Enter your marks : "))
std3 = int(input("Enter your marks : "))
std4 = int(input("Enter your marks : "))
std5 = int(input("Enter your marks : "))
std6 = int(input("Enter your marks : "))
mrk =[std1,std2,std3,std4,std5,std6]
mrk.sort()
print(mrk)

# write a program to sum a ist of four no.s
num = [3,5,2,8]
add = sum(num) # sum method for list.
# print(num[0]+num[1]+num[2]+num[3])
print(add)
print(sum(num))

#  write a program to count the zeros in the following tuple.
t = (92,45,0,4,98,0,0,0,4,22,14,0,67,59,50,0,0,7)
print(("The no. of zeros in the tuple are : "),t.count(0))



