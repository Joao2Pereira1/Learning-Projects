import pytest  # type:ignore

from app.utils.request import get_temperature


def test_get_content(mocker):
    mock_get = mocker.patch("app.utils.request.requests.get")
    mock_get.return_value.json.return_value = {"temperature": 25.5}

    temp = get_temperature("Salreu")

    # garante que a função processou a resposta mockada corretamente.
    assert temp == 25.5  # nosec

    # garante que a função construiu a URL certa.
    mock_get.assert_called_once_with("https://api.weatherapi.com/v1/forecast.json?key=a2e7082e845c48cfbb0123908250508&q=Salreu&days=7&aqi=no&alerts=no")
