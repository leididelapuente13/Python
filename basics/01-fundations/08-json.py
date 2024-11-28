import json

person = '{"name": "Aaron", "last_name": "Warner", "age": 19}'

# parse to json
person_json = json.loads(person)

# python dictionary to json
person = {"name": "Aaron", "last_name": "Warner", "age": 19}
person_json = json.dumps(person)

print(person_json)
