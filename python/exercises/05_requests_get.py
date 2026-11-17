# Exercise: send my first GET request to a public API and read the JSON reply.
# Needs: pip install requests
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)    # 200 means success
data = response.json()         # reply -> dict

print(data["title"])
print(data["completed"])
