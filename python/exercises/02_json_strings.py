# Exercise: convert a dict to a JSON string and back, and check the types.
import json

person = {"name": "Mohammed", "age": 20}

text = json.dumps(person)      # dict -> JSON string
print(text)
print(type(person))            # <class 'dict'>
print(type(text))              # <class 'str'>

back = json.loads(text)        # JSON string -> dict
print(back)
print(type(back))
print(back["name"])
