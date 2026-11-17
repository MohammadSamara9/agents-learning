# Exercise (solved on my own): request user 1 and print the name and email
# only if the status code is 200, otherwise print "request failed".
# Needs: pip install requests
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
data = response.json()

if response.status_code == 200:
    print(data["name"])
    print(data["email"])
else:
    print("request failed")

# Review note: safer to call response.json() inside the if, because a failed
# request may not return JSON.
