import requests

url = "https://api.aevo.xyz/trade-history"

headers = {
    "accept": "application/json",
    "AEVO_KEY": "Your key",
    "AEVO_SECRET": "Your secret"
}

response = requests.get(url, headers=headers)

print(response.text)