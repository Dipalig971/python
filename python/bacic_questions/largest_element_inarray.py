#Create a program to find the largest element in an array

arr=[3,4,5,6,7,8,9,20,70]

maximumNumber=arr[0]

for i in range(len(arr)):
    if arr[i]>maximumNumber:
     maximumNumber=arr[i]


print("Maximum number : ",maximumNumber)