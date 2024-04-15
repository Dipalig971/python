#Write a program to find the factorial of a number using functions.

x=int(input("Enter the number : "))
factorial=1
if x<0:
    print("Factorial does not exist negative value....")
elif x==0:
    print("The factorial of 0 is 1..")

else:
     for i in range(1,x+1):
         factorial=factorial*i

print("FActorial is : ",factorial)

