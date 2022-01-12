#. Create a class Time with private attributes hour, minute and second.
#Overload ‘+’ operator to find sum of 2 time.


class Time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self,a2):
        second=self.__second+a2.__second
        minute=self.__minute+a2.__minute
        hour=self.__hour+a2.__hour
        if(second>60):
            second=second-60
            minute=minute+1
        if(minute>60):
            minute=minute-60
            hour=hour+1
        return hour,minute,second
print("Enter time1:")
h1=int(input("hour:"))
m1=int(input("minute:"))
s1=int(input("second"))

t1=Time(h1,m1,s1)

print("Enter time2:")
h2=int(input("hour:"))
m2=int(input("minute:"))
s2=int(input("second"))

t2=Time(h2,m2,s2)

hr,min,sec=t1+t2
print(hr,end=":")
print(min,end=":")
print(sec,end=" ")

