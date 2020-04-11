x=int(input("Enter any number to check Prime Number"))

for i in range(2,int(x/2)):
    if(x%i==0):
        print(x, " Not a prime number")
        break
else:
    print(x," Prime number")