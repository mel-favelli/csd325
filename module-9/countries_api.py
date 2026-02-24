import requests
import json

url = "https://restcountries.com/v3.1/name/canada"
response = requests.get(url)

data = response.json()

country = data[0]

print("\nCountry Information")
print("---------------------")
print("Name:", country["name"]["common"])
print("Capital:", country["capital"][0])
print("Region:", country["region"])
print("Population:", country["population"])