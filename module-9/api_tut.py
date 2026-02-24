import requests

# Test connection to Google
response = requests.get('http://www.google.com')
print("Google Status Code:", response.status_code)

import requests
import json

# API for astronauts currently in space
url = "http://api.open-notify.org/astros.json"

response = requests.get(url)

print("Status Code:", response.status_code)

# Convert response to JSON
data = response.json()

print("\nNumber of people in space:", data["number"])
print("\nAstronauts currently in space:")

for person in data["people"]:
    print(person["name"], "-", person["craft"])