import requests

response = requests.get("https://api.kanye.rest/")

response.raise_for_status()

quote = response.json()

print(quote)