# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 480)
        MainWindow.setMinimumSize(QtCore.QSize(850, 450))

        # Estilo injetado no a partir do ficheiro python em vez de file.qss
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #F4F6F9;
            }
            QLabel {
                font-family: 'Segoe UI', Helvetica, Arial;
                color: #2C3E50;
            }
            QLineEdit {
                background-color: #FFFFFF;
                border: 1px solid #CBD5E1;
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 14px;
                color: #334155;
            }
            QLineEdit:focus {
                border: 2px solid #3B82F6;
                background-color: #FFFFFF;
            }
            QPushButton {
                background-color: #3B82F6;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 18px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #2563EB;
            }
            QPushButton:pressed {
                background-color: #1D4ED8;
            }
            QLabel#LocalLabel {
                font-size: 18px;
                font-weight: bold;
                color: #1E293B;
            }
            QLabel#LocalInfo {
                background-color: #E2E8F0;
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
                color: #475569;
            }
            /* Estilização dos Cards Semanais */
            QFrame[objectName^="card"] {
                background-color: #FFFFFF;
                border: 1px solid #E2E8F0;
                border-radius: 12px;
            }
            QLabel[objectName^="lbl_day"] {
                font-size: 14px;
                font-weight: bold;
                color: #64748B;
            }
            QLabel[objectName^="lbl_temp"] {
                font-size: 15px;
                font-weight: 600;
                color: #0F172A;
            }
            /* Menus e Barras */
            QMenuBar {
                background-color: #FFFFFF;
                border-bottom: 1px solid #E2E8F0;
                color: #334155;
            }
            QMenuBar::item:selected {
                background-color: #F1F5F9;
            }
            QMenu {
                background-color: #FFFFFF;
                border: 1px solid #E2E8F0;
            }
            QMenu::item:selected {
                background-color: #F1F5F9;
            }
        """)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Layout principal da janela
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(20, 20, 20, 20)
        self.mainLayout.setSpacing(15)

        # Zona Superior: Busca
        self.searchLayout = QtWidgets.QHBoxLayout()
        self.searchLayout.setSpacing(10)

        self.LocalLabel = QtWidgets.QLabel(self.centralwidget)
        self.LocalLabel.setObjectName("LocalLabel")
        self.searchLayout.addWidget(self.LocalLabel)

        self.LocalInput = QtWidgets.QLineEdit(self.centralwidget)
        self.LocalInput.setPlaceholderText("Digite a cidade (ex: Lisboa, London)...")
        self.searchLayout.addWidget(self.LocalInput)

        self.LocalButton = QtWidgets.QPushButton(self.centralwidget)
        self.LocalButton.setObjectName("LocalButton")
        self.searchLayout.addWidget(self.LocalButton)

        self.mainLayout.addLayout(self.searchLayout)

        # Zona Intermédia: Informaçoes extras do local ativo
        self.LocalInfo = QtWidgets.QLabel(self.centralwidget)
        self.LocalInfo.setObjectName("LocalInfo")
        self.LocalInfo.setWordWrap(True)
        self.mainLayout.addWidget(self.LocalInfo)

        # Zona Inferior: Título e Grid da Previsão Semanal
        self.Title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.Title.setFont(font)
        self.mainLayout.addWidget(self.Title)

        # Container dos Cards
        self.weekLayout = QtWidgets.QHBoxLayout()
        self.weekLayout.setSpacing(12)

        # Dados estruturados dos dias para criacao dinâmica e limpa dos cartoes
        self.days_data = [
            ("Segunda", "32ºC / 40ºC"),
            ("Terça", "22ºC / 30ºC"),
            ("Quarta", "18ºC / 30ºC"),
            ("Quinta", "10ºC / 20ºC"),
            ("Sexta", "30ºC / 40ºC"),
            ("Sábado", "12ºC / 22ºC"),
            ("Domingo", "30ºC / 40ºC"),
        ]

        # Loop de geracao dos cartoes verticais (Dia -> Ícone -> Temp)
        for i, (day_name, temp_val) in enumerate(self.days_data, 1):
            card = QtWidgets.QFrame(self.centralwidget)
            card.setObjectName(f"card_{i}")

            cardLayout = QtWidgets.QVBoxLayout(card)
            cardLayout.setContentsMargins(10, 15, 10, 15)
            cardLayout.setSpacing(10)
            cardLayout.setAlignment(QtCore.Qt.AlignCenter)

            lbl_day = QtWidgets.QLabel(day_name, card)
            lbl_day.setObjectName(f"lbl_day_{i}")
            lbl_day.setAlignment(QtCore.Qt.AlignCenter)
            cardLayout.addWidget(lbl_day)

            lbl_icon = QtWidgets.QLabel(card)
            lbl_icon.setObjectName(f"lbl_icon_{i}")
            lbl_icon.setMinimumSize(QtCore.QSize(48, 48))
            lbl_icon.setAlignment(QtCore.Qt.AlignCenter)
            # Placeholder para receber o QPixmap com o ícone da API de clima posteriormente
            lbl_icon.setText("---")
            cardLayout.addWidget(lbl_icon)

            lbl_temp = QtWidgets.QLabel(temp_val, card)
            lbl_temp.setObjectName(f"lbl_temp_{i}")
            lbl_temp.setAlignment(QtCore.Qt.AlignCenter)
            cardLayout.addWidget(lbl_temp)

            self.weekLayout.addWidget(card)

            # Guardando referências dinamicas no objeto para controle posterior via API
            setattr(self, f"day_{i}", lbl_day)
            setattr(self, f"icon_{i}", lbl_icon)
            setattr(self, f"temperature_{i}", lbl_temp)

        self.mainLayout.addLayout(self.weekLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        # Menubar e Statusbar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 25))
        self.menuClima = QtWidgets.QMenu(self.menubar)
        self.menuClima.setObjectName("menuClima")
        self.menuAcerca_de = QtWidgets.QMenu(self.menubar)
        self.menuAcerca_de.setObjectName("menuAcerca_de")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuClima.menuAction())
        self.menubar.addAction(self.menuAcerca_de.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Previsão do Tempo"))
        self.LocalLabel.setText(_translate("MainWindow", "Localização"))
        self.LocalButton.setText(_translate("MainWindow", "Procurar"))
        self.LocalInfo.setText(
            _translate(
                "MainWindow",
                "Aguardando pesquisa de localização... Aqui aparecerão coordenadas e vento.",
            )
        )
        self.Title.setText(_translate("MainWindow", "Previsão para a semana"))
        self.menuClima.setTitle(_translate("MainWindow", "Clima"))
        self.menuAcerca_de.setTitle(_translate("MainWindow", "Acerca de"))
