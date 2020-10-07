s1={"mon","tue","wed","thur",1}
print(s1)
# print tuple using for loop
for i in s1:
    print(i)
# using set() method
se2=set(["frid","saturday",1])
print(se2)
# add the element in s1 and update
s1.add("friday")
s1.update(["saturday","sunday"])
print(s1)
# remove and discard the elements from set
s1.discard("mon")
s1.remove("saturday")
print(s1)
# set operations on set
print(s1.union(se2))
print(s1.intersection(se2))
print(s1.difference(se2))
print(s1==se2)
print(s1>se2)
print(s1<se2)

#### frozen set
frozenset=frozenset([1,2,3,4,5])
for i in frozenset:
    print(i)