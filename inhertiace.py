# Grandparent class
class Grandparent:
    def __init__(self, name):
        self.name = name

    def show_family_origin(self):
        print(f"I am {self.name}, the grandparent of this family.")

# Parent class inherits from Grandparent
class Parent(Grandparent):
    def __init__(self, name, parent_name):
        # Call Grandparent's constructor
        super().__init__(parent_name)
        self.child_name = name

    def show_parent_info(self):
        print(f"I am {self.child_name}'s parent, child of {self.name}.")

# Child class inherits from Parent
class Child(Parent):
    def __init__(self, name, parent_name, grandparent_name):
        # Call Parent's constructor
        super().__init__(parent_name, grandparent_name)
        self.name = name

    def show_child_info(self):
        print(f"I am {self.name}, child of {self.child_name}, grandchild of {self.name}.")

    def introduce_family(self):
        print("\nFamily Introduction:")
        self.show_family_origin()
        self.show_parent_info()
        self.show_child_info()


# Create an object of Child class
child = Child("Charlie", "David", "Edward")

# Demonstrate inheritance
child.introduce_family()
