from typing import Tuple
from PySide6.QtGui import QFont, Qt
from PySide6.QtCore import QLine, QPropertyAnimation, QRect, QSize
from PySide6.QtWidgets import (
    QApplication, QLabel, QMainWindow, QPushButton, QWidget, QDialog, QVBoxLayout,
    QLineEdit, QHBoxLayout
)
from alerts import Alert
from exceptions import CannotBeZero, CannotBeNegative

class Font(QFont):
    def __init__(self) -> None:
        super().__init__()

        # fonte dos botoes principais
        self.fontMainButton = QFont()
        self.fontMainButton.setPointSize(16)
        self.fontMainButton.setBold(True)

        # fonte Label
        self.fontLabel = QFont()
        self.fontLabel.setPointSize(16)
        self.fontLabel.setBold(True)


class ButtonEffects():
    def buttonPressEffect(self, button: QPushButton) -> None:
        self.animation = QPropertyAnimation(button, b"geometry")
        self.animation.setDuration(20)
        self.animation.setStartValue(QRect(button.x(), button.y(), button.width(), 50))
        self.animation.setEndValue(QRect(button.x(), button.y(), button.width(), 52))
        self.animation.start()


    def buttonReleaseEffect(self, button: QPushButton) -> None:
        self.animation = QPropertyAnimation(button, b"geometry")
        self.animation.setDuration(20)
        self.animation.setStartValue(QRect(button.x(), button.y(), button.width(), 52))
        self.animation.setEndValue(QRect(button.x(), button.y(), button.width(), 50))
        self.animation.start()

    
    def centerWindow(self, widget: QWidget|QMainWindow) -> None:
        screen = QApplication.primaryScreen().availableGeometry()
        window = widget.geometry()
        x = (screen.width() - window.width()) // 2
        y = (screen.height() - window.height()) // 2
        widget.move(x, y)
    

class InputDialog(QDialog):
    def __init__(self, product_code: int, kg_or_unit_from_db: str = None) -> None:
        super().__init__()
        self.fonts = Font()
        self.alerts = Alert()

        self.setWindowTitle("Registrar Produto")
        self.setMinimumWidth(550)
        self.setMinimumHeight(150)
        self.setStyleSheet(
            "background-color: #A8D5BA;"
            "color: black;"
        )

        self.layout = QVBoxLayout(self)
        self.widgetWithLabelAndLineEdit = QWidget()
        self.layout.addWidget(self.widgetWithLabelAndLineEdit)

        horizontalLayout = QHBoxLayout(self.widgetWithLabelAndLineEdit)

        # variavel de controle para saber qual dado foi informado
        self.kg_or_unit = ""

        # widgetWithLabelAndLineEdit.setLayout(horizontalLayout)

        if kg_or_unit_from_db == "kg":  # produto vendido por peso
            labelKgPrice = QLabel()
            labelKgPrice.setText("Digite o peso em gramas: ")
            labelKgPrice.setFont(self.fonts.fontLabel)
            labelKgPrice.setMinimumWidth(100)
            labelKgPrice.setMinimumHeight(40)

            horizontalLayout.addWidget(labelKgPrice)

            self.valueLineEdit = QLineEdit()
            self.valueLineEdit.setMinimumHeight(40)
            self.valueLineEdit.setMinimumWidth(100)
            self.valueLineEdit.setStyleSheet(
                "border: 2px solid;"
                "border-radius: 10px;"
            )
            self.valueLineEdit.setTextMargins(10, 0, 0, 0)
            self.valueLineEdit.setPlaceholderText("Digite o peso...")
            horizontalLayout.addWidget(self.valueLineEdit)

            # se for kg
            self.kg_or_unit = "kg"
        else:  # produto vendido por unidade
            labelUnitPrice = QLabel()
            labelUnitPrice.setText("Digite a quantidade:")
            labelUnitPrice.setFont(self.fonts.fontLabel)
            labelUnitPrice.setMinimumWidth(100)
            labelUnitPrice.setMinimumHeight(40)
            
            horizontalLayout.addWidget(labelUnitPrice)

            self.valueLineEdit = QLineEdit()
            self.valueLineEdit.setPlaceholderText("Informe a quantidade.")
            self.valueLineEdit.setMinimumHeight(40)
            self.valueLineEdit.setMinimumWidth(100)
            self.valueLineEdit.setStyleSheet(
                "border: 2px solid;"
                "border-radius: 10px;"
            )
            self.valueLineEdit.setTextMargins(10, 0, 0, 0)  
            horizontalLayout.addWidget(self.valueLineEdit)

            # se for unit
            self.kg_or_unit = "un"

        # botao de confirmar o peso ou quantidade
        confirmButton = QPushButton("Confirmar")
        # confirmButton.setMinimumHeight(50)
        confirmButton.setFixedSize(QSize(200, 50))
        confirmButton.setFont(self.fonts.fontMainButton)
        confirmButton.setStyleSheet(
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
        confirmButton.clicked.connect(self.checkInputValue)
        self.layout.addWidget(confirmButton, alignment=Qt.AlignCenter)

        # self.setLayout(layout)


    def getValue(self) -> Tuple[str, float]:
        lineEditValue = float(self.valueLineEdit.text())

        return self.kg_or_unit, lineEditValue


    def checkInputValue(self) -> None:
        # pegando o input do usuário
        inputValueText = self.valueLineEdit.text()

        # verificando se o valor inserido pode ser um float ou um int
        try:
            if "," in inputValueText:
                inputValueText = inputValueText.replace(",", ".")

            inputValue = float(inputValueText)

            if inputValue == 0:
                raise CannotBeZero("O valor não pode ser igual a zero.")
            
            elif inputValue < 0:
                raise CannotBeNegative("O valor não pode ser negativo.")

            self.accept()
        except ValueError as err:
            self.valueLineEdit.clear()
            self.alerts.showAlert(1)
        
        except (CannotBeZero, CannotBeNegative) as err:
            self.valueLineEdit.clear()
            self.alerts.showAlert(3, str(err))
