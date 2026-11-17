# Exercise: write a dict to a JSON file, then read it back.
import json

person = {"name": "Mohammed", "age": 20}

with open("person.json", "w") as f:
    json.dump(person, f)

with open("person.json", "r") as f:
    data = json.load(f)

print(data)
print(data["age"])
