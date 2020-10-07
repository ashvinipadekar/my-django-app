"""
d1={"name":"ash","middle":"datta","lastname":"padekar"}
print(d1)
#  To print the your choice values by using key
print(d1["middle"])
print(d1.get("name"))
###  MOdify the values
d1["middle"]="popat"
print(d1)

### TO  use for loop for showing the keys and values
for i in d1:
    print(i)
### To print values using for loop
for i in d1:
    print(d1[i])
### To print keys and values from the dictionaries
for x,y in d1.items():
    print(x,y)
### To check whether the key present or not
if "name" in d1:
    print("yes")
#### To add items to dictionary
d1["son"]="rihu"
print(d1)
#### To remove items from dictionary
d1.pop("name")
print(d1)
"""

### To print dictionaries within dictionaries

mydic={
    "child1":{"name":"A","age ":20},
    "child2":{"name":"B","age":30},
    "child3":{"name":"c","age":40}
}
print(mydic)

c1={"name ":"ash","age":56}
c2={"name":"sucheta","age":60}
c3={"name":"sonia","age":65}
mychild={"childs1":c1,"child2":c2,"child3":c3}
print(mychild)