"""
***program odd even program
num=int(input("enter no"))
if num%2==0:
    print("num is even")
else:
    print("num is odd")

***program to find which number is grater
a=int(input("enter value of a"))
b=int(input("enter value of b"))
c=int(input("enter value of c"))
if a>b and a>c:
    print("number is a")
elif b>a and b>c:
    print("number is b")
else:
    print("number is c")

*** program to find whether eligible for vote or not
age = int(input("enter age"))
if age >= 18:
    print("eligible for vote")
else:
    print("not eligible for vote")


*** program to find out grade occured in exam
marks=int(input("enter the markes "))
if marks>85 and marks<=100:
    print("enter grade A")
elif marks>60 and marks<=85:
    print("you will  get grade B+")
elif marks>40 and marks<=60:
    print("you will gate grate B")
elif marks>30 and marks<=40:
    print(" you will gate grade C")
else:
    print(" you are fail in exam")

**** program to find out digit of a number
num=int(input("enter number"))
if num>=0 and num<10:
    print("number is one digit")
elif num>=10 and num<100:
    print("number is two digit")
elif num>=100 and num<1000:
    print("number is three digit")
elif num>=1000 and num<10000:
    print("number is four digit")
else:
    print("number digit not found")
"""