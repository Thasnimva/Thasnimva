x=int(input("enter 1st no"))
y=int(input("enter 2nd no"))
i=1
while(i<=x and i<=y):
    if(x%i==0 and y%i==0):
        gcd=i
    i=i+1
print("gcd:",gcd)    
