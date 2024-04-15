#Write a program to check if a string is a palindrome

str1=str(input("Enter name : "))

if(str1==str1[::-1]):
    print("String is Palindrome")
else:
    print("String is not Palindrome")