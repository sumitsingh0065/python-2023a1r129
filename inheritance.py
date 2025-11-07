# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

# Child class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Another child class
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Access inherited and overridden methods
print(dog.name, "says", dog.speak())  # Buddy says Woof!
print(cat.name, "says", cat.speak())  # Whiskers says Meow!