#write a program to swap two number without using temporary variable

x=int(input("Enter the value of X : "))
y=int(input("Enter the value of Y : "))

x=x+y
y=x-y
x=x-y

print("X=",x)
print("y=",y)