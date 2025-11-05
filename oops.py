# Define a class
class Animal:
    def __init__(self, name, species):
        self.name = name        # attribute
        self.species = species  # attribute

    def make_sound(self):
        return "Some generic sound"

    def info(self):
        return f"{self.name} is a {self.species}."


# Inheritance: Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")  # call parent constructor
        self.breed = breed

    # Polymorphism: same method name, different behavior
    def make_sound(self):
        return "Woof!"

    def fetch(self, item):
        return f"{self.name} fetched the {item}!"


# Another derived class
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def make_sound(self):
        return "Meow!"


# Create objects
dog1 = Dog("Buddy", "Golden Retriever")
cat1 = Cat("Whiskers", "White")

# Access methods
print(dog1.info())
print(dog1.make_sound())
print(dog1.fetch("ball"))

print(cat1.info())
print(cat1.make_sound())
