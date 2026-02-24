import requests

def get_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()[0]

    return {
        "official_name": data["name"]["official"],
        "capital": data.get("capital", ["N/A"])[0],
        "region": data.get("region", "N/A"),
        "subregion": data.get("subregion", "N/A"),
        "population": data.get("population", "N/A"),
        "currencies": ", ".join(data.get("currencies", {}).keys()),
        "languages": ", ".join(data.get("languages", {}).values()),
        "timezones": ", ".join(data.get("timezones", [])),
        "latlng": data.get("latlng", [0, 0])
    }

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()
    return data.get("current_weather", {})