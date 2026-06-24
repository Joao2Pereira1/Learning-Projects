"""
WeatherService for the weather application.

This module handles the request to the weather api, to get the forecast
of the weather in a specific location for the next 7 days and it also formats
 and returns the weather data, so it can be used in the main window controller.
"""

import datetime
import json

import requests  # type: ignore
from model.weather_data import LocationData, WeatherData

WEEK_DAYS_TRANSLATOR = {
            "Monday": "Segunda",
            "Tuesday": "Terça",
            "Wednesday": "Quarta",
            "Thursday": "Quinta",
            "Friday": "Sexta",
            "Saturday": "Sábado",
            "Sunday": "Domingo",
        }

WEEK_DAYS = ["Segunda","Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]

class WeatherService:
    """ class responsible to do the request to weather api, and
    formatting data to be able to use it after."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.content = None

    def fetch_forecast(self, local: str) -> bool:
        """
        Makes a request to the API to get forecast data for the next week.

        Args:
            local (str): Location name (not case sensitive).

        Returns:
            bool:
                True if the request was successful and the content was stored.
                False if the request failed.
        """

        url = f"https://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={local}&days=7&aqi=no&alerts=no"
        try:
            response = requests.get(url, timeout=10)
            if 200 <= response.status_code < 300:
                self.content = json.loads(response.content)
                return True
            return False
        except Exception:
            return False

    def get_location_info(self) -> LocationData | None:
        """
        Returns more details about the location.

        Returns:
            LocationData: class with attributes name,region, country e hour.

            None: if no content is available.
        """

        # info about local selected and hour
        if self.content:
            loc = self.content["location"]
            return LocationData(
                name=loc["name"],
                region=loc["region"],
                country=loc["country"],
                local_time=loc["localtime"]
            )
        print("Não existe nenhum conteudo sobre o tempo.")
        return None

    def get_forecast(self) -> tuple[str, dict[str, WeatherData]] | None:
        """
        Returns the forecast weather to the next 7 days.

        Returns:
            tuple: (actual_day, forecast), where:
                - actual_day (str): day of the week, e.g., "Monday".
                - forecast (dict): {"YYYY-MM-DD": [max, min, average, condition, icon]}.

            None: if no content is available
        """

        if not self.content:
            return None

        # forecast_day it will be a list with the forecast for 7 days
        forecast_list = self.content["forecast"]["forecastday"]
        forecast_dict = {}

        current_day = datetime.date.today().strftime("%A") # returns monday,tuesday,...
        current_day = WEEK_DAYS_TRANSLATOR[current_day] # translates to portuguese

        # each item on the list represents the forecast for that day
        for item in forecast_list:
            day_info = item["day"]
            forecast_dict[item["date"]] = WeatherData(
                date=item["date"],
                max_temp=day_info["maxtemp_c"],
                min_temp=day_info["mintemp_c"],
                avg_temp=day_info["avgtemp_c"],
                state=day_info["condition"]["text"],
                icon_url=day_info["condition"]["icon"],
            )
        return current_day, forecast_dict
