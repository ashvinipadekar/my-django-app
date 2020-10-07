class Animal:
    def speak(self):
        print("animal speakong")


class Dog(Animal):
    def bark(self):
        print("Dog barking")


class ChildDog(Dog):
    def eat(self):
        print("child dog eating")


d= ChildDog()
d.speak()
d.bark()
d.eat()
