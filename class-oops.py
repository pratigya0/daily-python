# Blueprint
'''class Dog:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says Woof!")

# Actual object
dog1 = Dog("Tommy", 3)
dog2 = Dog("Bruno", 5)

dog1.bark()   # Tommy says Woof!
dog2.bark()   # Bruno says Woof!'''



'''class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi I am {self.name} and I am {self.age} old")

s1 = Student("Pratigya", 23)
s1.introduce()

s2 = Student("jiya", 21)
s2.introduce()'''



'''# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating!")

# Child class — inherits Animal!
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

# Object
d1 = Dog("Tommy")
d1.eat()    # ✅ inherited from Animal!
d1.bark()   # ✅ Dog's own method! '''


#Create —

#Parent class Vehicle with method move()
#Child class Car that inherits Vehicle and adds method honk()

