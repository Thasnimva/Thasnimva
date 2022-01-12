class publisher:

  def __init__(self,pname):
    self.pname=pname

  def display(self):
   print("Publisher Name:",self.pname)

class book(publisher):

  def get(self,title,author):
    self.title=title
    self.author=author
    
  def display(self):
   print("Title Name:",self.title)
   print("Author Name:",self.author)

class python(book):

 def __init__(self,price,nop,pname):
  super().__init__(pname)
  self.price=price
  self.nop=nop

 def details(self):
  print("Price:",self.price)
  print("No of pages:",self.nop)

s1=python(450,72,"K D")
s1.get("Flames","K D")
s1.display()
s1.details()



