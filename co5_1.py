# 1. Write a Python program to read a file line by line and store it into a list.

f1=open("firstfile.txt","w")
f1.write("This is my first file in python.\nWant to work with files.\n This is my third")
f1.close()

f1=open("firstfile.txt","r")
f1.seek(0,0)
ff=f1.readlines()
for x in range(0,len(ff)):
    print(ff[x])

print()
#f1.seek(0,0)
#ff=f1.readlines()  #return list of all lines
print(ff)

f1.close()
