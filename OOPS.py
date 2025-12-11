# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "This animal makes a sound."


# Derived class (Inheritance)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# Using the classes
dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")

print(dog1.speak())
print(cat1.speak())
