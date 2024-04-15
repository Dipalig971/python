#Create a program to find the sum of digits of a number using recursion.


def sumofdigit(x):
    if x< 10:
        return x
    else:
        return x%10 + sumofdigit(x/10)

# Read number
number = int(input("Enter number: "))

# Function call
sum = sumofdigit(number)

# Display output
print("Sum of digit of number :", sum)