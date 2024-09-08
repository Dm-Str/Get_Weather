import requests

url = "https://wttr.in/"
options = "?MTnq&lang=ru"
payload = {
    "CYXU": "Лондон",
    "SVO": "Шереметьево",
    "ULWC": "Череповец",
}


def get_weather() -> None:
    for i in payload:
        response = requests.get(url + payload[i] + options)
        response.raise_for_status()
        print(response.text)


if __name__ == "__main__":
    get_weather()
