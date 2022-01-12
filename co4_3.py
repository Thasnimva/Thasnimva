# Create a class Rectangle with private attributes length and width.
#Overload ‘<’ operator to compare the area of 2 rectangles

class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def __lt__(self,a1):
        area1=self.length*self.width
        area2=a1.length*a1.width
        if(area1>area2):
            return(True)
        else:
            return(False)
        
        
print("Enter the Details of Rectangle:1")
l1=int(input("Length:"))
w1=int(input("width:"))
r1=rectangle(l1,w1)
print("Enter the Details of Rectangle:2")
l2=int(input("Length:"))
w2=int(input("width:"))
r2=rectangle(l2,w2)
if(r1>r2):
    print("Rectangle 2 is larger!!")
else:
    print("Rectangle 1 is larger!!")

