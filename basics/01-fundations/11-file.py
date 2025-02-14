import os

# open a file
file = open('./assets/text.txt', 'r')

# read a file
# print(file.read())

# read characters of the file
# print(file.read(1))

# read a line of the file
print(file.readline())

# close file
file.close()

# create a file
file_secondary = open("./assets/text-secondary.txt", "w")
file_secondary.write("New file")
file_secondary.close()
file_secondary_content = open("./assets/text-secondary.txt", "r")
print(file_secondary_content.read())
file_secondary_content.close()

# delete file
if os.path.exists("./assets/text-secondary.txt"):
    os.remove("./assets/text-secondary.txt")
else:
    print("This file does not exist")