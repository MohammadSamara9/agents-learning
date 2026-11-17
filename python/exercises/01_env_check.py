# Exercise: read an API key from a .env file and check that it exists.
# Needs: pip install python-dotenv, and a .env file with API_KEY=... (never commit it)
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("API_KEY")

if key is None:
    print("no key found")
else:
    print("key is uploaded")
