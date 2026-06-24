import requests  # type:ignore


def get_temperature(local) -> float:
    url = f"https://api.weatherapi.com/v1/forecast.json?key=a2e7082e845c48cfbb0123908250508&q={local}&days=7&aqi=no&alerts=no"
    response = requests.get(url)  # nosec
    data = response.json()
    return data["temperature"]
