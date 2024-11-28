name = "John Doe"

# prints the first letter
print(name[0])

# how to loop a string
for letter in name:
    print(letter)

# how to know the length of a string
print(len(name))

paragraph = "To check if a certain phrase or character is present in a string, we can use the keyword in."
print("." in paragraph)

# checking if something is in the array with if
if "." in paragraph:
    print(". is in the paragraph")

# checking if something is not in a string
print("to" not in paragraph)

if "To" not in paragraph:
    print("It is not")

### WHAT ARE THE METHODS TO MODIFY STRINGS
last_name = "warner"
print(last_name.upper())
print(last_name.lower())
# how to remove white spaces in a string in the beginning and end
word = " Hello World "
print(word.strip())

## how to replace a string with another string
print(word.strip().replace("Hello", "Goodbye"))

## covert string to a list
print(word.strip().split(" "))

## interpolation
age = 12
name = 'Leidi'
full_name = "Hello, my name is {a} and I'm {b} ".format(a = name, b = age)

print(full_name)
txt = f"My age is {age}"
print(txt)

## logical operators

# and = &&
# or = ||
# not = !

## identity operators

# is ===
# is not !===