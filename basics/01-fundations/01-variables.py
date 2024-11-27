# Variables

x = 5
y = 3
z = "Variable"

print(type(z))

LastName = "Warner"
lastName = "Warner"
last_name = "Warner"

# Unpacking a collection
fruits = ["Banana", "Cherry", "Strawberry"]
a, b, c = fruits
print(a, b, c)

# Global variables

var = "Global"

def myfunc():
    print("This is a function who can access to:", var)

myfunc()

# Create global variable inside a function

def function():
    global variable
    variable = "fantastic"

function()
print(variable)

# use global to modify a global variable inside a function

animal = "Dog"

def dog_function():
    global animal = "Cat"