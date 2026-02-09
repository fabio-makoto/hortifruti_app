from PySide6.QtGui import QFont
from PySide6.QtCore import QPropertyAnimation, QRect
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget


class Font(QFont):
    def __init__(self) -> None:
        super().__init__()

        # fonte dos botoes principais
        self.fontMainButton = QFont()
        self.fontMainButton.setPointSize(16)
        self.fontMainButton.setBold(True)


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