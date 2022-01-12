#Create Rectangle class with attributes length and breadth and methods to find area and perimeter.
#Compare two Rectangle objects by their area.

class Rectangle:
    def __init__(self,length,breadth,ar):
        self.length=length
        self.breadth=breadth
        self.ar=0
    def area(self):
        self.ar=self.length*self.breadth
        #print("area=",self.ar)
        return (self.ar)

    def perimeter(self):
        self.perimeter=2*(self.length+self.breadth)
        #print(perimeter)
        return (self.perimeter)

    def display(self):
        print("area=",self.ar)
        print("perimeter=",self.perimeter)
        

R1=Rectangle(2,4,0)
R2=Rectangle(3,4,0)

R1.area()
R1.perimeter()

R2.area()
R2.perimeter()
print("Area of Rectangle1")
R1.display()

print("Area of Rectangle2")
R2.display()


if (R1.ar>R2.ar):
    print(R1.ar,"is graeter")
else:
    print(R2.ar,"is greater")