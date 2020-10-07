li = [3, 4, 7, 8, 9, 3, 2]
# for i in li:
li.append(10)
# in insert we can pass the position and actual value of any number
li.insert(1, 13)
li.remove(10)
li.pop(0)
li.__delitem__(0)
# del li
# li.clear()
li1=li.copy()
new = list(li)
print(new)
print(new+li1)
li.reverse()
print(li)
li.sort()
print(li)
x=li.count(2)
print(x)
