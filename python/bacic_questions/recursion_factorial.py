#Create a program to find the factorial of a number using recursion.

def factorial(i):
    if i==0 or i==1:
        return 1
    else:
        return i*factorial(i-1)

i=int(input("Enter number : "))
print("Factorial is : ",factorial(i))