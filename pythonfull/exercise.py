"""
Progarm no 23
def square(num):
    return num**2
print(square(2))
print(square(3))

#### Program no 25
class Add:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name =={} and age==={}".format(self.name,self.age) )
d=Add("ashvini",30)
d.display()
#### to print sum of 2 nos
def sum(a,b):
    return a+b
print(sum(10,20))

### to print the string of integer value
def str1(n):
    print(str(n))
str1(3)
### To define function of two integer numbers in string format and compute their sum:
def number(s1,s2):
    print(int(s1)+int(s2))
number(10,30)

 #### To define function of two string values concatinate them and print the result
def add(s1,s2):
    print(s1+s2)
add("3","4")

### To  define fn to accept two string and print maximum lenght console& if two string same print all string line by line
def printstring(s1,s2):
    len1=len(s1)
    len2=len(s2)
    if len1>len2:
        print(s1)
    elif len1<len2:
        print(s2)
    else:
        print(s1)
        print(s2)
printstring("ashvini","datta")


#### even or not
def evenno(n1):

    if n1 % 2 == 0:
        print("even")
    else:
        print("odd")


evenno(13)
"""
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print(li)

