#Create a program to check if a given number is prime.

n=int(input("Enter the value of n : "))
i=2
temp=0

while i<=n/2:        
        if(n%i==0):
            temp=0
            i+=1
            break

        if n==1:
            print("1 is neither prime nor composite")
        else:
            if temp==0:
                  print(n,"is prime number.....")
            else:
                  print(n,"This is not prime number.....")
                