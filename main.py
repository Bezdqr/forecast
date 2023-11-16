import requests

url = "https://wttr.in"
params = {
    "Tn": "",
    "lang": "ru"
}

response = requests.get(url, params=params)
print(response.text)
