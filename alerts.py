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
            case 4:  # caixa de dialogo para confirmar a finalizacao da venda
                self.msgConfirm = QMessageBox()
                self.msgConfirm.setWindowTitle("Confirmação")
                self.msgConfirm.setText("Deseja finalizar a venda?")
                self.msgConfirm.setIcon(QMessageBox.Information)

                self.buttonSim = self.msgConfirm.addButton("Sim", QMessageBox.YesRole)
                self.buttonNao = self.msgConfirm.addButton("Não", QMessageBox.NoRole)

                self.msgConfirm.setDefaultButton(self.buttonSim)
                self.msgConfirm.exec()
            case 5:  # mensagem de erro personalizada
                QMessageBox.information(QWidget(), "Atenção", msg)