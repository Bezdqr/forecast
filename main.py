import requests


def main():
    url = "https://wttr.in"
    params = {
        "Tn": "",
        "lang": "ru"
    }

    response = requests.get(url, params=params)
    print(response.text)


if __name__ == "__main__":
    main()
