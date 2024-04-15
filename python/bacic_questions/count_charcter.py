#Create a program to count the occurrence of a character in a string.

string="dipaligunjalsunil"
#string=str(input("Enter any string : "))

count=0

for i in string:
    if i=='a':
        count=count+1


print("count the occurrence of a character : " + str(count))