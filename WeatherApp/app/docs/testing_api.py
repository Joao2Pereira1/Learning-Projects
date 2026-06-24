import pytest  # type:ignore
import requests  # type:ignore

url = "https://api.weatherapi.com/v1/current.json?key=a2e7082e845c48cfbb0123908250508&q=London&aqi=no"
request = requests.get(url)  # nosec

print(f"\nStatus code: {request.status_code}\n\n")
print(f"Headers: {request.headers}\n\n")
print(f"Content: {request.content}\n\n")
print(f"Text: {request.text}\n")

#! usar mock do pytest para testar