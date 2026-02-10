from PySide6.QtWidgets import QMessageBox, QWidget


class Alert():
    def showAlert(self, num: int, msg: str = None) -> None:
        match num:
            case 1:  # valor informado é inválido
                QMessageBox.critical(QWidget(), "Erro", "O valor informado é inválido. Tente novamente...")
            case 2:  # campo do codigo do produto vazio
                QMessageBox.information(QWidget(), "Atenção", "Digite o código do produto.")
            case 3:  # mesangem de erro personalizada
                QMessageBox.critical(QWidget(), "Atenção", msg)