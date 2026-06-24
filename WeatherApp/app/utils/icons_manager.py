"""
IconsManager module for the weather application.

This module handles the download and local storage of weather condition icons.
Icons are cached locally to avoid repeated network requests, improving performance
and reducing unnecessary API calls.
"""

import os

import requests  # type: ignore


class IconsManager:
    """
    Responsible to manage icons dictionary:
    - Verifies if icon is saved locally.
    - Does the download from request url and saves new icons locally.
    -> Basically it serves as cache to improve performance.
    """

    def __init__(self, folder_path: str = "app/icons", dict_path: str = "app/model/icons_dict.txt"):
        self.icons_folder = folder_path
        self.dict_path = dict_path
        os.makedirs(self.icons_folder, exist_ok=True)
        self.weather_icons = self.load_dict()


    def load_dict(self)-> dict | str:
        """
        Loads dictionary from the file, because when the program
        resets, it looses the dictionary data.

        Returns:
            Dict: to check if operation was successful.
        """

        weather_icons = {}

        if not os.path.exists(self.dict_path):
            return {}

        with open(self.dict_path, "r", encoding="utf-8") as f:
            for line in f:
                icon, path = line.strip().split(",", 1)
                weather_icons[icon] = path
        return weather_icons


    def save_dict(self) -> str:
        """
        Saves dictionary: dict{"sunny":"icons/sunny.png"}.

        Returns:
            Message: to check if operation was successful.
        """

        try:
            with open(self.dict_path,"w", encoding="utf-8") as f:
                for icon,path in self.weather_icons.items():
                    f.write(f"{icon},{path}\n") # separado por virgula
            return True
        except FileNotFoundError as e:
            message = f"Couldn't find file to save dictionary:{e}"
        except PermissionError as e:
            message = f"No permission to save dictionary in this file:{e}"
        return message


    def get_weather_icon_path(self,weather_state: str, weather_icon_url: str) -> str|None:
        """
        Responsible to get the icons associated to the weather state,
        if it's present in the dictionary, otherwise new icon is added.

        Args:
            weather_state (str): weather state, if it's sunny, rainy, ...
            weather_icon_url(str):  icon url to do the request to save the icon png.
        Raises:
            Exception: in case the file is not downloaded.
        Returns:
            str: The local path to the saved icon, so it can be loaded in the GUI.

            None: in case it happened some error.
        """

        image_path = None

        if weather_state not in self.weather_icons:
            print(weather_icon_url)
            response = requests.get(f"https:{weather_icon_url}", timeout=10)  # nosec
            print(response)

            if response.status_code == 200:
                # Heavy Sunny -> lower and replace space by _
                image_path = weather_state.lower().replace(" ", "_") + ".png"
                image_path = f"app/icons/{image_path}"
                with open(image_path, "wb") as f:
                    f.write(response.content)
                self.weather_icons[weather_state] = image_path
                self.save_dict()
            else:
                raise Exception(f"Erro ao baixar imagem: {response.status_code}")
        else:
            image_path = self.weather_icons[weather_state]
        return image_path
