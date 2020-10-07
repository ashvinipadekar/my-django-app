d={'name':'ashvini','age':30}
print("name is %s and age is %d "%(d["name"],d["age"]))
d['name']="datta"
d["company"]="mgm"

for x in d:
    print(x)
    print(d.get(x))
    for x,y in d.items():
        print(x,y)
print("name is %s and age is %d"%(d.get("name"),d.get("age")))