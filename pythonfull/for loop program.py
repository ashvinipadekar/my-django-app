"""
 *** program to print python stmt
str="python"
for i in str:
    print(i)

*** program to print table for  given no
list=[1,2,3,4,5,6,7,8,9,10]
n=5
for i in list:
    c=i*n
    print(c)


*** To print sum of  given numbers
list=[10,20,30,40,50,60]
sum=0
for i in list:
    sum=sum+i
    print("sum of numbers="+str(sum))

**** to print range for given no
for i in range(10):
    print(i)

*** to print the table for given number using range function

num=int(input("enter the number"))
for i in range(1,11):
    c=num*i
    print(num,"*",i,"=",c)

*** to print even numbers upto given number using range function
num=int(input("enter the number"))
for i in range(2,num,2):
    print(i)

***** To print pyramid numbers

rows=int(input("enter the number"))
for i in range(rows):
    for j in range(i):
        print(i, end=" ")  # print number
    # line after each row to display pattern correctly
    print(" ")
output
enter the number 5
1
2 2
3 3 3
4 4 4 4

*** to print * in pyramid

num=int(input("enter the numbers"))
for i in range(num):
    for j in range(i):
        print("*",end="")
    print()
  #output num=5
  *
  **
  ***
  ****

 **** To print numbers in reverse order:

num=int(input("enter the numbers"))
for i in range(1,num+1):
    for j in range(i,num+1):
        print(j,end="")
    print("")
 o/p: num=3
 123
 23
 3
*** To print diamond in shapes
rows = 5
for row in range(1, rows+1):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")
    o/p:
    1
    12
    123
    1234
    12345

**** To print reverse pyramid
111
22
3

rows = 3
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')
**** To print inverted pyramid with same no
333
33
3

rows = 3
num = rows
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")
"""
num = 6
for row in range(1, num+1 ):
    #for colum in range(1, row+ 1):
     for j in range(row):
        print(row , end="")

     print("")
