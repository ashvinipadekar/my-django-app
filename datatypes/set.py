s={10,20,30,40}
s1=set(s)
print(s1)
s.add(50)
s.pop()
#s.pop()
print(s)
s2={1,2,3,4,10}
print(s|s2)
print(s.union(s2))

print(s&s2)
print(s-s2)
print(s<s2)
print(s>s2)
print(s==s2)
