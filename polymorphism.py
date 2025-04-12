class Animal:
    def __init__(self, name):
        self.name = name
        
    def move(self):
        return "Generic animal movement"

class Fish(Animal):
    def move(self):
        return f"{self.name} is swimming! 🐟"

class Bird(Animal):
    def move(self):
        return f"{self.name} is flying! 🦅"

class Snake(Animal):
    def move(self):
        return f"{self.name} is slithering! 🐍"

# Demonstration
animals = [
    Fish("Nemo"),
    Bird("Eagle"),
    Snake("Python")
]

for animal in animals:
    print(animal.move())