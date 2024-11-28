person = {
    "name": "John",
    "last_name": "Doe",
    "age": 19,
    "hobbies": ["read", "listen to music", "play the guitar"]
}

# get properties
person_name = person.get("name");
print(person_name)

# update properties
person.update({"age": 20})

# add properties
person["favorite_color"] = "blue"

# remove property
person.pop("favorite_color")
# del person["favorite_color"]
print(person)

# remove dictionary
# del person

# clear the dictionary
# person.clear()

# loop dictionary properties
for attributes in person:
    print(attributes)

# loop dictionary values
for property_value in person:
    print(person[property_value])

for attribute_value in person.values():
    print(attribute_value)

# nested elements
parent = {
    "name": "Nothing",
    "mother": {
        "name": "None"
    },
    "father": {
        "name": "None"
    }
}

print(parent)