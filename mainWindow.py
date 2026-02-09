# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QCloseEvent, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow, QMessageBox,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

import sys

from tools import Font, ButtonEffects

from pointOfSaleWindow import Ui_mainWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setStyleSheet(
            u"background-color: #A8D5BA;"
            "color: #013220;"
            )
        MainWindow.setWindowIcon(QIcon("images/logo.png"))
        MainWindow.window().closeEvent = self.closeWindow

        self.fonts = Font()
        self.effects = ButtonEffects()

        self.effects.centerWindow(MainWindow)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalMainLayout = QVBoxLayout(self.centralwidget)
        self.verticalMainLayout.setObjectName(u"verticalMainLayout")

        # widget com os botoes
        self.widgetWithButtons = QWidget(self.centralwidget)
        self.widgetWithButtons.setObjectName(u"widgetWithButtons")
        self.widgetWithButtons.setMaximumSize(QSize(16777215, 100))
        self.widgetWithButtons.setStyleSheet(
            "border: 2px solid #006400;"
            "border-radius: 20px;"
        )

        self.horizontalLayoutWithButtons = QHBoxLayout(self.widgetWithButtons)
        self.horizontalLayoutWithButtons.setObjectName(u"horizontalLayoutWithButtons")
        self.horizontalSpacerFirst = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutWithButtons.addItem(self.horizontalSpacerFirst)

        # botao de cadastrar
        self.registerButton = QPushButton(self.widgetWithButtons)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setMinimumSize(QSize(0, 50))
        self.registerButton.setStyleSheet(
            "QPushButton {"
            "border: 2px solid #006400;\n"
            "border-radius: 10px;\n"
            "background-color: #FF7518;\n"
            "}\n"
            "QPushButton:hover {\n"
                "background-color: #FFE5B4"
            "}\n"
            "QPushButton:Pressed {\n"
                "font-size: 22px;\n"
                "background-color: #FBC4AB\n"
            "}"
            )
        self.registerButton.setFont(self.fonts.fontMainButton)

        self.horizontalLayoutWithButtons.addWidget(self.registerButton)

        self.horizontalSpacerSecond = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutWithButtons.addItem(self.horizontalSpacerSecond)

        # botao de vender
        self.openPosButton = QPushButton(self.widgetWithButtons)
        self.openPosButton.setObjectName(u"openPosButton")
        self.openPosButton.setMinimumSize(QSize(0, 50))
        self.openPosButton.setStyleSheet(
            "QPushButton {"
            "border: 2px solid #006400;\n"
            "border-radius: 10px;\n"
            "background-color: #FF7518;\n"
            "}\n"
            "QPushButton:hover {\n"
                "background-color: #FFE5B4"
            "}\n"
            "QPushButton:Pressed {\n"
                "font-size: 22px;\n"
                "background-color: #FBC4AB\n"
            "}"
            )
        self.openPosButton.setFont(self.fonts.fontMainButton)
        self.openPosButton.clicked.connect(self.openPointOfSaleWindow)

        self.horizontalLayoutWithButtons.addWidget(self.openPosButton)

        self.horizontalSpacerThird = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutWithButtons.addItem(self.horizontalSpacerThird)

        # botao de relatorios
        self.reportButton = QPushButton(self.widgetWithButtons)
        self.reportButton.setObjectName(u"reportButton")
        self.reportButton.setMinimumSize(QSize(0, 50))
        self.reportButton.setStyleSheet(
            "QPushButton {"
            "border: 2px solid #006400;\n"
            "border-radius: 10px;\n"
            "background-color: #FF7518;\n"
            "}\n"
            "QPushButton:hover {\n"
                "background-color: #FFE5B4"
            "}\n"
            "QPushButton:Pressed {\n"
                "font-size: 22px;\n"
                "background-color: #FBC4AB\n"
            "}"
            )
        self.reportButton.setFont(self.fonts.fontMainButton)

        self.horizontalLayoutWithButtons.addWidget(self.reportButton)

        self.horizontalSpacerFourth = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutWithButtons.addItem(self.horizontalSpacerFourth)

        self.verticalMainLayout.addWidget(self.widgetWithButtons)

        # label com a logo da página
        self.labelWithLogo = QLabel(self.centralwidget)
        self.labelWithLogo.setObjectName(u"label")
        self.labelWithLogo.setPixmap(QPixmap("images/logo.png"))
        self.labelWithLogo.setScaledContents(True)
        self.labelWithLogo.setStyleSheet(
            "border: 2px solid #006400;"
            "border-radius: 20px;"
        )

        self.verticalMainLayout.addWidget(self.labelWithLogo)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.allButtons = [
            self.reportButton, self.openPosButton, self.registerButton
        ]

        self.allWindows = []

        for button in self.allButtons:
            button.pressed.connect(lambda b=button: self.effects.buttonPressEffect(b))
            button.released.connect(lambda b=button: self.effects.buttonReleaseEffect(b))
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Horti Mkt", None))
        self.registerButton.setText(QCoreApplication.translate("MainWindow", u"CADASTRO", None))
        self.openPosButton.setText(QCoreApplication.translate("MainWindow", u"VENDER", None))
        self.reportButton.setText(QCoreApplication.translate("MainWindow", u"RELATORIOS", None))
        # self.labelWithLogo.setText(QCoreApplication.translate("MainWindow", u"LOGO", None))
    # retranslateUi


    def closeWindow(self, event: QCloseEvent) -> None:
        msg = QMessageBox()
        msg.setWindowTitle("Confirmação")
        msg.setText("Deseja realmente fechar o sistema?")
        msg.setIcon(QMessageBox.Question)

        buttonSim = msg.addButton("Sim", QMessageBox.YesRole)
        buttonNao = msg.addButton("Não", QMessageBox.NoRole)

        msg.setDefaultButton(buttonNao)
        msg.exec()

        if msg.clickedButton() == buttonSim:
            for window in self.allWindows:
                window.close()

            event.accept()
        else:
            event.ignore()


    def openPointOfSaleWindow(self) -> None:
        self.pointOfSaleWindow = QWidget()
        self.uiPointOfSaleWindow = Ui_mainWidget()
        self.uiPointOfSaleWindow.setupUi(self.pointOfSaleWindow)
        self.pointOfSaleWindow.showMaximized()

        self.allWindows.append(self.pointOfSaleWindow)


app = QApplication(sys.argv)
mainWindow = QMainWindow()
uiMainWindow = Ui_MainWindow()
uiMainWindow.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec())
