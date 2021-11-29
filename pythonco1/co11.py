x=int(input("enter 1st number"))
y=int(input("enter 2nd number:"))
z=int(input("enter 3rd number"))
if(x>y) and (x>z):
    largest=x
elif(y>x) and (y>z):
    largest=y
else:
    largest=z
print("largest no is",largest)    
