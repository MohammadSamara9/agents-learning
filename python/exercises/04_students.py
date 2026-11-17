# Exercise (solved on my own): save a list of 3 students to students.json,
# read the file again, and print the name of each student.
import json

students = [{"name": "mohammed", "age": 20},
            {"name": "ali", "age": 19},
            {"name": "bob", "age": 18}]


with open("students.json", "w") as f:
    json.dump(students, f)


with open("students.json", "r") as f:
    text = json.load(f)

for student in text:
    print(student["name"])

# Review note: `text` holds a list, so a name like `loaded_students` would be clearer.
