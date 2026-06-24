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


class MainWindowController(QMainWindow):
    """ Main window controller will be responsible to update
    the gui when something happens. """

    def __init__(self):
        """
        self → the main window (QMainWindow) that will be displayed on the screen.

        Ui_MainWindow → the interface class created in Qt Designer.

        self.ui.setupUi(self) → method of the Ui_MainWindow class
        that takes a window (QMainWindow) as an argument and is responsible
        for adding the widgets created in Qt Designer
        into the main window (self).
        """

        super().__init__()  # inherits QMainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ? gerir eventos
        self.ui.LocalButton.clicked.connect(self.get_local_input)

        # < Instancias das classes
        self.weather_service = WeatherService("a2e7082e845c48cfbb0123908250508")
        self.icons_manager = IconsManager()

        # add action to menu acerca to show some info
        self.info_action = self.ui.menuAcerca_de.addAction("Sobre")
        self.info_action.triggered.connect(self.sobre_pressed)

        # overrides the default keyPressEvent method of LocalInput to the
        # new method self.key_press_event and receives the same arg QKeyEvent -> e
        self.ui.LocalInput.keyPressEvent = self.key_press_event

        # objetos da ui
        self.days: List[QLabel] = [
            self.ui.day1, self.ui.day2, self.ui.day3,
            self.ui.day4, self.ui.day5, self.ui.day6, self.ui.day7
        ]
        self.icons: List[QLabel] = [
            self.ui.icon1, self.ui.icon2, self.ui.icon3,
            self.ui.icon4, self.ui.icon5, self.ui.icon6, self.ui.icon7
        ]
        self.temperatures: List[QLabel] = [
            self.ui.temperature1, self.ui.temperature2, self.ui.temperature3,
            self.ui.temperature4, self.ui.temperature5, self.ui.temperature6, self.ui.temperature7
        ]

    def sobre_pressed(self):
        message = QMessageBox(self)
        message.setText("Isto é uma simples aplicação que mostra a previsão do clima nos próximos 7 dias.")
        message.exec()

    def key_press_event(self, e: QKeyEvent)-> None:
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
            print('enter/return')
            self.get_local_input()

        # it calls the default behavior of QLineEdit (insert text etc.)
        QLineEdit.keyPressEvent(self.ui.LocalInput, e)

    def get_local_input(self) -> None:
        """ it will receive the local input and then show the data at GUI"""

        print("Botao clicado!")

        local = self.ui.LocalInput.text()
        print(local)

        # makes request
        response = self.weather_service.fetch_forecast(local)

        if response == True:
            # show data about the local
            location_data = self.weather_service.get_location_info() # returns Location class
            self.ui.LocalInfo.setText(str(location_data))

            # returns a tuple(current day, dictionary with weather data for each day)
            current_day, forecast = self.weather_service.get_forecast()

            # used annotations to see the methods
            day:str
            weather: WeatherData

            # get current day index in WEEK_DAYS
            day_index = WEEK_DAYS.index(current_day)

            # show data about the forecast
            i = 0
            for day, weather in forecast.items():
                if day_index == 7:
                    day_index = 0
                    self.days[i].setText(f"{day}\n  {WEEK_DAYS[day_index]}")
                else:
                    self.days[i].setText(f"{day}\n  {WEEK_DAYS[day_index]}")
                icon_path = self.icons_manager.get_weather_icon_path(weather.state, weather.icon_url)
                self.icons[i].setPixmap(QPixmap(icon_path))
                self.temperatures[i].setText(f"{weather.min_temp}  {weather.max_temp}")
                i += 1
                day_index +=1
        else:
            alert = QMessageBox(self)
            alert.setText('Local inserido inválido.')
            alert.exec()
            self.ui.LocalInput.setText("")
            print("Local inserido inválido.")
