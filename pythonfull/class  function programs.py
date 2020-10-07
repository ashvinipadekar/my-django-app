def add(a, b):
    print(a + b)


add(10, 20)

### to create a class and create object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)



class Abc:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def mycall(self):
        print("my name is==="+self.name)
a=Abc("ash",30)
a.mycall()