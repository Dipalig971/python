#Write a program to find the GCD (Greatest Common Divisor) of two numbers.

x=int(input("Enter num1 : "))
y=int(input("Enter num2 : "))
GCD=1

for i in range(1,min(x,y)):
    if x%1==0 and y%1==0:
        GCD=i

print("GCD of ",x,"and",y,"is",GCD )