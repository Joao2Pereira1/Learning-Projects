"""
Main window controller for the weather application.

This module handles the interaction between the UI components and the
business logic, updating widgets with weather data, handling user input,
and managing signals and slots for the main application window.
"""

from typing import List

from model.weather_data import WeatherData
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent, QMouseEvent, QPixmap
from PyQt5.QtWidgets import QLabel, QLineEdit, QMainWindow, QMessageBox
from services.weather_service import WEEK_DAYS, WeatherService
from ui.gui import Ui_MainWindow  # UI design for the application
from utils.icons_manager import IconsManager
import os
from dotenv import load_dotenv


class MainWindowController(QMainWindow):
    """Main window controller will be responsible to update
    the gui when something happens."""

    def __init__(self):
        """
        self → the main window (QMainWindow) that will be displayed on the screen.
        Ui_MainWindow → the interface class created in Qt Designer.

        self.ui.setupUi(self) → method of the Ui_MainWindow class
        that takes a window (QMainWindow) as an argument and is responsible
        for adding the widgets created in Qt Designer
        into the main window (self).
        """
        load_dotenv()
        api_key = os.getenv("API_KEY")

        super().__init__()  # inherits QMainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ? Gerir eventos
        self.ui.LocalButton.clicked.connect(self.get_local_input)

        # < Instancias das classes
        self.weather_service = WeatherService(api_key)
        self.icons_manager = IconsManager()

        # add action to menu acerca to show some info
        self.info_action = self.ui.menuAcerca_de.addAction("Sobre")
        self.info_action.triggered.connect(self.sobre_pressed)

        # overrides the default keyPressEvent method of LocalInput to the
        # new method self.key_press_event and receives the same arg QKeyEvent -> e
        self.ui.LocalInput.keyPressEvent = self.key_press_event

        # objetos da ui
        self.days: List[QLabel] = [
            self.ui.day_1,
            self.ui.day_2,
            self.ui.day_3,
            self.ui.day_4,
            self.ui.day_5,
            self.ui.day_6,
            self.ui.day_7,
        ]
        self.icons: List[QLabel] = [
            self.ui.icon_1,
            self.ui.icon_2,
            self.ui.icon_3,
            self.ui.icon_4,
            self.ui.icon_5,
            self.ui.icon_6,
            self.ui.icon_7,
        ]
        self.temperatures: List[QLabel] = [
            self.ui.temperature_1,
            self.ui.temperature_2,
            self.ui.temperature_3,
            self.ui.temperature_4,
            self.ui.temperature_5,
            self.ui.temperature_6,
            self.ui.temperature_7,
        ]

    def sobre_pressed(self):
        message = QMessageBox(self)
        message.setText(
            "Isto é uma simples aplicação que mostra a previsão do clima nos próximos 7 dias."
        )
        message.exec()

    def key_press_event(self, e: QKeyEvent) -> None:
        """
        Responsible to when the user presses key return, it calls
        the function get_local_input().

        Args:
            e (QKeyEvent): a keyboard event
        """

        print(type(e))  # class 'PyQt5.QtGui.QKeyEvent'>
        print(e.key())  # key code
        print("event", e)

        if e.key() in (Qt.Key_Return, Qt.Key_Enter):
            print("enter/return")
            local = self.get_local_input()
            if local:
                self.retrieve_weather_data(local)

        # it calls the default behavior of QLineEdit (insert text etc.)
        QLineEdit.keyPressEvent(self.ui.LocalInput, e)

    def get_local_input(self) -> None:
        """
        It will get the local input.
        Local Input is the LineEdit responsible to get city or place.
        """

        # print("Botao clicado!")

        local = self.ui.LocalInput.text()
        return local

    def retrieve_weather_data(self, local) -> None:
        """It will receive the local input and then show the data at GUI."""

        response = self.weather_service.fetch_forecast(local)

        if response == True:
            location_data = self.weather_service.get_location_info()
            self.ui.LocalInfo.setText(str(location_data))

            # returns a tuple(current day, dictionary with weather data for each day)
            current_day, forecast = self.weather_service.get_forecast()

            day: str
            weather: WeatherData

            # get current day index in WEEK_DAYS
            day_index = WEEK_DAYS.index(current_day)

            print(forecast.items)
            # show data about the forecast -> [day: weather data]
            i = 0
            for day, weather in forecast.items():
                print(weather)
                if day_index == 7:
                    day_index = 0
                    self.days[i].setText(f"{day}\n  {WEEK_DAYS[day_index]}")
                else:
                    self.days[i].setText(f"{day}\n  {WEEK_DAYS[day_index]}")
                icon_path = self.icons_manager.get_weather_icon_path(
                    weather.state, weather.icon_url
                )
                self.icons[i].setPixmap(QPixmap(icon_path))
                self.temperatures[i].setText(f"{weather.min_temp}  {weather.max_temp}")
                i += 1
                day_index += 1
        else:
            alert = QMessageBox(self)
            alert.setText("Local inserido inválido.")
            alert.exec()
            self.ui.LocalInput.setText("")
            print("Local inserido inválido.")
