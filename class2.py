class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def move(self):
        print(f"the {self.name} car, which is {self.color} color")

class Car (Vehicle):
    def honk(self):
        print(f"press honk the {self.name}")
    
d1 = Car("Dezire", "pink")
d1.move()
d1.honk()