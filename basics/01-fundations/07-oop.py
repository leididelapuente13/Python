class Person:
    def __init__(self, name, age, married):
        self.name = name
        self.age = age
        self.married = married

    def __str__(self):
        return f"{self.name}, {self.age}"




myPerson = Person("Nothing", 12, False)
print(myPerson.__str__())

class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def print_name(self):
        print(self.name)

class Dog(Animal):
    def __init__(self, name, age, color, fluffy):
        super().__init__(self, name, age)
        self.color = color
        self.fluffy = fluffy

    def print_name(self):
        print(self.name, self.fluffy)

    def bark(self):
        print("Woof", self.name)
