# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pointOfSaleWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from typing import Any, Callable, List, Tuple, TypeVar
import mysql.connector
from mysql.connector import Error
from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from tools import InputDialog, Font
from db_connect import DataBaseConnection
from alerts import Alert
from exceptions import CannotBeNegative, CannotBeZero, DataNotFound, DataAlreadyExists

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)


F = TypeVar("F", bound=Callable[..., Tuple[MySQLConnection, MySQLCursor]])


def close_connection(func: F) -> Callable[..., None]:
    def wrapper(self, *args: Any, **kwargs: Any) -> None:
        conn, cur = func(self, *args, **kwargs)
        self.db.closeDb(conn, cur)
        return None
    return wrapper


class Ui_mainWidget(object):
    def setupUi(self, mainWidget):
        self.db = DataBaseConnection()
        self.alerts = Alert()
        self.fonts = Font()

        if not mainWidget.objectName():
            mainWidget.setObjectName(u"mainWidget")
        # mainWidget.resize(1280, 720)
        mainWidget.setMinimumSize(QSize(1280, 650))
        mainWidget.setStyleSheet(
            "background-color: #A8D5BA;"
            "color: black;"
            )

        self.formLayout = QFormLayout(mainWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.widgetWithTopLabelLineEdit = QWidget(mainWidget)
        self.widgetWithTopLabelLineEdit.setObjectName(u"widgetWithTopLabelLineEdit")
        self.widgetWithTopLabelLineEdit.setMinimumSize(QSize(1000, 100))
        self.gridLayout = QGridLayout(self.widgetWithTopLabelLineEdit)
        self.gridLayout.setObjectName(u"gridLayout")

        # label do codigo
        self.codeLabel = QLabel(self.widgetWithTopLabelLineEdit)
        self.codeLabel.setObjectName(u"codeLabel")
        self.codeLabel.setFont(self.fonts.fontPosLabel)
        self.codeLabel.setMaximumHeight(50)

        self.gridLayout.addWidget(self.codeLabel, 0, 0, 1, 1)

        # line edit do código 
        self.codeLineEdit = QLineEdit(self.widgetWithTopLabelLineEdit)
        self.codeLineEdit.setObjectName(u"codeLineEdit")
        self.codeLineEdit.setMinimumSize(QSize(400, 0))
        self.codeLineEdit.setMaximumHeight(50)
        self.codeLineEdit.returnPressed.connect(self.processProduct)
        self.codeLineEdit.setFont(self.fonts.fontPosLabel)
        self.codeLineEdit.setStyleSheet(
            "border: 2px solid black;"
            "border-radius: 5px;"
            "background-color: #66BB6A;"
        )
        self.codeLineEdit.setTextMargins(10, 0, 0, 0)

        self.gridLayout.addWidget(self.codeLineEdit, 0, 1, 1, 1)


        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.widgetWithTopLabelLineEdit)

        self.widgetWithTopButtons = QWidget(mainWidget)
        self.widgetWithTopButtons.setObjectName(u"widgetWithTopButtons")
        self.gridLayout_2 = QGridLayout(self.widgetWithTopButtons)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        # botao de cancelar venda
        self.cancelSaleButton = QPushButton(self.widgetWithTopButtons)
        self.cancelSaleButton.setStyleSheet(
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
        self.cancelSaleButton.setFont(self.fonts.fontMainButton)

        self.gridLayout_2.addWidget(self.cancelSaleButton, 0, 0, 1, 1)

        # botao de remover produto
        self.removeProductButton = QPushButton(self.widgetWithTopButtons)
        self.removeProductButton.setStyleSheet(
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
        self.removeProductButton.setFont(self.fonts.fontMainButton)
        self.removeProductButton.setText("Remover produto")
        self.removeProductButton.clicked.connect(self.removeProduct)

        self.gridLayout_2.addWidget(self.removeProductButton, 1, 0, 1, 1)


        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.widgetWithTopButtons)

        self.widgetWithTable = QWidget(mainWidget)
        self.widgetWithTable.setObjectName(u"widgetWithTable")
        self.widgetWithTable.setMinimumSize(QSize(1000, 0))
        self.verticalLayout = QVBoxLayout(self.widgetWithTable)
        self.verticalLayout.setObjectName(u"verticalLayout")

        # tabela de produtos
        self.productTable = QTableWidget(self.widgetWithTable)
        self.productTable.setMinimumWidth(1000)
        self.productTable.setMinimumHeight(300)
        self.productTable.setFont(self.fonts.tableFontContent)
        self.productTable.setStyleSheet(
            """
            QTableWidget::item::selected {
                background-color: #FF6961;
            }
            QTableWidget {
                border: 2px solid black;
                border-radius: 6px;
            }
            """
        )
        self.productTable.verticalHeader().setMinimumWidth(30)
        self.insertColumnOnTable()

        self.verticalLayout.addWidget(self.productTable)

        # widget com as labels do valor total da venda
        self.widgetWithTotalSale = QWidget(self.widgetWithTable)
        self.widgetWithTotalSale.setObjectName(u"widgetWithTotalSale")
        self.widgetWithTotalSale.setMaximumSize(QSize(16777215, 85))

        self.horizontalLayout = QHBoxLayout(self.widgetWithTotalSale)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        # label do titulo do total da venda
        self.labelWithTotalSale = QLabel(self.widgetWithTotalSale)
        self.labelWithTotalSale.setMaximumSize(QSize(150, 70))
        self.labelWithTotalSale.setFont(self.fonts.fontTotalSaleValue)

        self.horizontalLayout.addWidget(self.labelWithTotalSale)

        # label com o valor total da venda
        self.labelWithTotalSaleValue = QLabel(self.widgetWithTotalSale)
        self.labelWithTotalSaleValue.setObjectName(u"labelWithTotalSaleValue")
        self.labelWithTotalSaleValue.setStyleSheet(
            "border: 2px solid black;"
            "border-radius: 10px;"
            "background-color: #66BB6A;"
        )
        self.labelWithTotalSaleValue.setFont(self.fonts.fontTotalSaleValue)
        self.labelWithTotalSaleValue.setMinimumHeight(70)
        self.labelWithTotalSaleValue.setContentsMargins(10, 0, 0, 0)

        self.horizontalLayout.addWidget(self.labelWithTotalSaleValue)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        # label do titulo do troco
        self.labelWithChange = QLabel(self.widgetWithTotalSale)
        self.labelWithChange.setObjectName(u"labelWithChange")
        self.labelWithChange.setFont(self.fonts.fontTotalSaleValue)
        self.labelWithChange.setMaximumSize(QSize(100, 70))

        self.horizontalLayout.addWidget(self.labelWithChange)

        # label do troco com o valor
        self.labelWithChangeValue = QLabel(self.widgetWithTotalSale)
        self.labelWithChangeValue.setObjectName(u"labelWithChangeValue")
        self.labelWithChangeValue.setMinimumHeight(70)
        self.labelWithChangeValue.setContentsMargins(10, 0, 0, 0)
        self.labelWithChangeValue.setFont(self.fonts.fontTotalSaleValue)
        self.labelWithChangeValue.setStyleSheet(
            "border: 2px solid black;"
            "border-radius: 10px;"
            "background-color: #66BB6A;"
        )

        self.horizontalLayout.addWidget(self.labelWithChangeValue)


        self.verticalLayout.addWidget(self.widgetWithTotalSale)


        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.widgetWithTable)

        self.widgetWithPaymentMethod = QWidget(mainWidget)
        self.widgetWithPaymentMethod.setObjectName(u"widgetWithPaymentMethod")
        self.verticalLayout_2 = QVBoxLayout(self.widgetWithPaymentMethod)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        # label do titulo da forma de pagamento
        self.labelPaymentMethods = QLabel(self.widgetWithPaymentMethod)
        self.labelPaymentMethods.setObjectName(u"labelPaymentMethods")
        self.labelPaymentMethods.setFont(self.fonts.fontLabel)
        self.labelPaymentMethods.setMaximumHeight(30)

        self.verticalLayout_2.addWidget(self.labelPaymentMethods)

        # combo box das formas de pagamento
        self.paymentMethodsComboBox = QComboBox(self.widgetWithPaymentMethod)
        self.paymentMethodsComboBox.setObjectName(u"comboBox")
        self.paymentMethodsComboBox.setFont(self.fonts.fontLabel)
        self.paymentMethodsComboBox.currentTextChanged.connect(self.enabledDisabledLineEdit)
        self.getComboBoxItems()

        self.verticalLayout_2.addWidget(self.paymentMethodsComboBox)

        self.widgetWithValueInstallments = QWidget(self.widgetWithPaymentMethod)
        self.widgetWithValueInstallments.setObjectName(u"widgetWithValueInstallments")
        self.gridLayout_3 = QGridLayout(self.widgetWithValueInstallments)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        # label da quantidade de vezes
        self.labelInstallments = QLabel(self.widgetWithValueInstallments)
        self.labelInstallments.setObjectName(u"labelInstallments")
        self.labelInstallments.setFont(self.fonts.fontLabel)
        self.labelInstallments.setAlignment(Qt.AlignRight)

        self.gridLayout_3.addWidget(self.labelInstallments, 0, 0, 1, 1)

        # line edit das quantidade de vezes
        self.installmentsLineEdit = QLineEdit(self.widgetWithValueInstallments)
        self.installmentsLineEdit.setObjectName(u"installmentsLineEdit")
        self.installmentsLineEdit.setFont(self.fonts.fontLabel)
        self.installmentsLineEdit.setStyleSheet(
            "border: 2px solid black;"
            "border-radius: 6px;"
        )
        self.installmentsLineEdit.setTextMargins(10, 0, 0, 0)
        self.installmentsLineEdit.setDisabled(True)

        self.gridLayout_3.addWidget(self.installmentsLineEdit, 0, 1, 1, 1)

        # label do valor que foi pago
        self.labelValue = QLabel(self.widgetWithValueInstallments)
        self.labelValue.setObjectName(u"labelValue")
        self.labelValue.setFont(self.fonts.fontLabel)
        self.labelValue.setAlignment(Qt.AlignRight)

        self.gridLayout_3.addWidget(self.labelValue, 1, 0, 1, 1)

        # line edit do valor pago
        self.valueLineEdit = QLineEdit(self.widgetWithValueInstallments)
        self.valueLineEdit.setObjectName(u"valueLineEdit")
        self.valueLineEdit.setFont(self.fonts.fontLabel)
        self.valueLineEdit.setStyleSheet(
            "border: 2px solid black;"
            "border-radius: 6px;"
        )
        self.valueLineEdit.setTextMargins(10, 0, 0, 0)

        self.gridLayout_3.addWidget(self.valueLineEdit, 1, 1, 1, 1)

        self.verticalLayout_2.addWidget(self.widgetWithValueInstallments)

        # botao de adicionar forma de pagamento
        self.addPaymentMethodButton = QPushButton(self.widgetWithValueInstallments)
        self.addPaymentMethodButton.setObjectName(u"addPaymentMethodButton")
        self.addPaymentMethodButton.setStyleSheet(
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
        self.addPaymentMethodButton.setFont(self.fonts.fontMainButton)
        self.addPaymentMethodButton.clicked.connect(self.addPaymentMethod)

        self.gridLayout_3.addWidget(self.addPaymentMethodButton, 2, 1, 1, 1)

        # self.verticalLayout_2.addWidget(self.addPaymentMethodButton)

        # label do titulo do valor total recebido
        self.labelTotalReceived = QLabel(self.widgetWithValueInstallments)
        self.labelTotalReceived.setObjectName(u"labelTotalReceived")
        self.labelTotalReceived.setFont(self.fonts.fontLabel)

        self.gridLayout_3.addWidget(self.labelTotalReceived, 3, 0, 1, 1)

        # label do valor total recebido
        self.labelTotalReceivedLabel = QLabel(self.widgetWithValueInstallments)
        self.labelTotalReceivedLabel.setObjectName(u"labelTotalReceivedLabel")
        self.labelTotalReceivedLabel.setFont(self.fonts.fontLabel)
        self.labelTotalReceivedLabel.setMaximumHeight(30)
        self.labelTotalReceivedLabel.setStyleSheet(
            "border: 2px solid black;"
            "border-radius: 6px;"
        )

        self.gridLayout_3.addWidget(self.labelTotalReceivedLabel, 3, 1, 1, 1)

        # label do titulo do valor restante a receber
        self.labelRemainingAmountToReceive = QLabel(self.widgetWithValueInstallments)
        self.labelRemainingAmountToReceive.setText("Valor Restante: R$")
        self.labelRemainingAmountToReceive.setFont(self.fonts.fontLabel)
        self.labelRemainingAmountToReceive.setMaximumHeight(30)
        
        self.gridLayout_3.addWidget(self.labelRemainingAmountToReceive, 4, 0, 1, 1)

        # label do valor restante a receber
        self.labelRemainingAmountToReceiveValue = QLabel(self.widgetWithValueInstallments)
        self.labelRemainingAmountToReceiveValue.setText("")
        self.labelRemainingAmountToReceiveValue.setFont(self.fonts.fontLabel)
        self.labelRemainingAmountToReceiveValue.setMaximumHeight(30)
        self.labelRemainingAmountToReceiveValue.setStyleSheet(
            "border: 2px solid black;"
            "border-radius: 6px;"
        )

        self.gridLayout_3.addWidget(self.labelRemainingAmountToReceiveValue, 4, 1, 1, 1)

        # botao de excluir formas de pagamento
        self.deletePaymentMethods = QPushButton(self.widgetWithValueInstallments)
        self.deletePaymentMethods.setText("Excluir Pagamentos")
        self.deletePaymentMethods.setFont(self.fonts.fontMainButton)
        self.deletePaymentMethods.setMaximumHeight(30)
        self.deletePaymentMethods.setStyleSheet(
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
        self.deletePaymentMethods.clicked.connect(self.deletePayment)

        self.gridLayout_3.addWidget(self.deletePaymentMethods, 5, 0, 1, 2)

        # botao de pagar a compra
        self.payButton = QPushButton(self.widgetWithValueInstallments)
        self.payButton.setText("Pagar")
        self.payButton.setFont(self.fonts.fontMainButton)
        self.payButton.setMaximumHeight(30)
        self.payButton.setStyleSheet(
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
        self.payButton.clicked.connect(self.paySale)

        self.gridLayout_3.addWidget(self.payButton, 6, 0, 1, 2)

        # widget is blank for spacing
        self.labelBlank = QLabel(self.widgetWithValueInstallments)
        self.labelBlank.setText("")
        self.verticalLayout_2.addWidget(self.labelBlank)

        self.gridLayoutWithSaleNumber = QGridLayout()
        self.verticalLayout_2.addLayout(self.gridLayoutWithSaleNumber)

        # label do titulo do numero da venda
        self.saleNumberTitleLabel = QLabel()
        self.saleNumberTitleLabel.setText("Venda Nº:")
        self.saleNumberTitleLabel.setFont(self.fonts.fontLabel)
        self.saleNumberTitleLabel.setMaximumHeight(30)

        self.gridLayoutWithSaleNumber.addWidget(self.saleNumberTitleLabel, 0, 0, 1, 1, alignment=Qt.AlignRight)

        # label com o numero da venda
        self.saleNumberLabel = QLabel()
        self.saleNumberLabel.setText("")
        self.saleNumberLabel.setFont(self.fonts.fontLabel)
        self.saleNumberLabel.setMaximumHeight(30)
        self.saleNumberLabel.setStyleSheet(
            "border: 2px solid black;"
            "border-radius: 6px;"
        )

        self.getNumberSale()

        self.gridLayoutWithSaleNumber.addWidget(self.saleNumberLabel, 0, 1, 1, 1)



        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.widgetWithPaymentMethod)


        self.retranslateUi(mainWidget)

        QMetaObject.connectSlotsByName(mainWidget)

        self.allProductsAdded = []
        self.remainingValue = 0
        self.totalReceived = 0
        self.hiddenShowWidget("notPay")
    # setupUi

    def retranslateUi(self, mainWidget: QWidget) -> None:
        mainWidget.setWindowTitle(QCoreApplication.translate("mainWidget", u"Frente de Caixa", None))
        self.codeLabel.setText(QCoreApplication.translate("mainWidget", u"C\u00d3DIGO:", None))
        self.codeLineEdit.setPlaceholderText(QCoreApplication.translate("mainWidget", u"Insira o c\u00f3digo do produto", None))
        self.cancelSaleButton.setText(QCoreApplication.translate("mainWidget", u"Cancelar Venda", None))
        self.labelWithTotalSale.setText(QCoreApplication.translate("mainWidget", u"Total R$:", None))
        self.labelWithChange.setText(QCoreApplication.translate("mainWidget", u"Troco:", None))
        self.labelPaymentMethods.setText(QCoreApplication.translate("mainWidget", u"Formas de pagamento:", None))
        self.labelInstallments.setText(QCoreApplication.translate("mainWidget", u"Vezes:", None))
        self.labelValue.setText(QCoreApplication.translate("mainWidget", u"Valor: R$", None))
        self.addPaymentMethodButton.setText(QCoreApplication.translate("mainWidget", u"Adicionar", None))
        self.labelTotalReceived.setText(QCoreApplication.translate("mainWidget", u"Total Recebido: R$", None))
    # retranslateUi


    @close_connection
    def processProduct(self) -> Tuple[MySQLConnection, MySQLCursor]:
        self.conn = self.db.connectDb()
        self.cur = self.conn.cursor(buffered=True)

        userInputCode = self.codeLineEdit.text()

        # verificando se o código digitado é válido
        if len(userInputCode) == 0:
            self.codeLineEdit.clear()
            self.alerts.showAlert(2)

        elif len(userInputCode) > 0:
            try:
                productCode = int(userInputCode)

                selectQuery = (
                    "SELECT p.product_code, p.name, p.cost_price, p.sell_price,\n"
                    "p.quantity, pt.name\n"
                    "FROM products as p\n"
                    "JOIN product_type AS pt ON p.id_product_type = pt.id\n"
                    f"WHERE p.product_code = {productCode} "
                )

                try:
                    self.cur.execute(selectQuery)

                    # checando se foi encontrado algum resultado
                    if self.cur.rowcount == 0:
                        raise DataNotFound(f"Não existe nenhum produto com o código {productCode}!")
                    
                except (mysql.connector.Error, DataNotFound) as err:
                    self.codeLineEdit.clear()
                    self.alerts.showAlert(3, str(err))  # mensagem de erro personalizada
                
                else:
                    product = self.cur.fetchone()
                    print(product)
                    productName = product[1]
                    kg_or_unit_from_db = product[5]
                    sellPrice = product[3]

                    dialog = InputDialog(productName, userInputCode, kg_or_unit_from_db)

                    if dialog.exec():
                        valueType, value = dialog.getValue()
                        print(f"Tipo do valor {valueType=}")
                        print(f"Valor: {value=}")

                        finalPrice = self.calculatePrice(valueType, value, sellPrice)

                        print(f"preço final: {finalPrice:.2f}")

                        self.addProduct(product, value, finalPrice)
                        self.codeLineEdit.clear()

            except ValueError as err:
                self.codeLineEdit.clear()
                self.alerts.showAlert(1)

        return self.conn, self.cur


    def calculatePrice(self, productType: str, inputValue: float, sellPrice: float) -> float:
        if productType == "kg":
            finalPrice = (inputValue / 1000) * sellPrice
        else:
            finalPrice = inputValue * sellPrice
        
        return finalPrice

    
    def addProduct(self, product: List|Tuple, userInputValue: float, totalValue: float) -> None:
        # informações
        # código, produto, preço un/kg, qtd/peso, valor total
        productCode = product[0]
        productName = product[1]
        productSellPrice = product[3]
        productType = product[5]
        # adicionando o nome do produto na lista de produto adicionados
        try:
            if productName in self.allProductsAdded:
                productName = productName.upper()
                raise DataAlreadyExists(f"O produto {productName} já foi registrado.")

        except DataAlreadyExists as err:
            self.alerts.showAlert(3, str(err))
        
        else:
            self.allProductsAdded.append(productName)

            productList = [productCode, productName, productSellPrice, userInputValue, totalValue]

            self.insertItemsOnTable(productList, productType)

            # sempre que um produto foi adicionado, será somado o valor dele ao 
            # valor total da compra
            self.sumTotalPrice()
            print(f"{self.allProductsAdded=} \n {productList=}")


    def insertItemsOnTable(self, productList: List|Tuple, productType: str) -> None:
        row = len(self.allProductsAdded)

        self.productTable.setRowCount(row)

        if productType == "kg":
            codeValue = QTableWidgetItem(str(productList[0]))
            codeValue.setTextAlignment(Qt.AlignCenter)
            nameValue = QTableWidgetItem(productList[1])
            sellPriceValue = QTableWidgetItem(f"R${productList[2]:.2f}kg")
            quantityValue = QTableWidgetItem(f"{productList[3]:.0f}gr")
            totalValue = QTableWidgetItem(f"R${productList[4]:.2f}")
        else:
            codeValue = QTableWidgetItem(str(productList[0]))
            codeValue.setTextAlignment(Qt.AlignCenter)
            nameValue = QTableWidgetItem(productList[1])
            sellPriceValue = QTableWidgetItem(f"R${productList[2]:.2f}un")
            quantityValue = QTableWidgetItem(f"{productList[3]:.0f}un")
            totalValue = QTableWidgetItem(f"R${productList[4]:.2f}")

        codeValue.setFlags(codeValue.flags() &~Qt.ItemIsEditable)
        nameValue.setFlags(nameValue.flags() &~Qt.ItemIsEditable)
        sellPriceValue.setFlags(sellPriceValue.flags() &~Qt.ItemIsEditable)
        quantityValue.setFlags(quantityValue.flags() &~Qt.ItemIsEditable)
        totalValue.setFlags(totalValue.flags() &~Qt.ItemIsEditable)

        if row == 1:
            self.productTable.setItem(0, 0, codeValue)
            self.productTable.setItem(0, 1, nameValue)
            self.productTable.setItem(0, 2, sellPriceValue)
            self.productTable.setItem(0, 3, quantityValue)
            self.productTable.setItem(0, 4, totalValue)
        else:
            self.productTable.setItem(row - 1, 0, codeValue)
            self.productTable.setItem(row - 1, 1, nameValue)
            self.productTable.setItem(row - 1, 2, sellPriceValue)
            self.productTable.setItem(row - 1, 3, quantityValue)
            self.productTable.setItem(row - 1, 4, totalValue)

    
    def insertColumnOnTable(self) -> None:
        self.productTable.setColumnCount(5)

        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(self.fonts.tableFontHeader);
        __qtablewidgetitem.setText("CÓDIGO");
        self.productTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(self.fonts.tableFontHeader);
        __qtablewidgetitem1.setText("PRODUTO");
        self.productTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)

        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(self.fonts.tableFontHeader);
        __qtablewidgetitem2.setText("PREÇO UN/KG");
        self.productTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)

        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(self.fonts.tableFontHeader);
        __qtablewidgetitem3.setText("QTD/PESO");
        self.productTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)

        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(self.fonts.tableFontHeader);
        __qtablewidgetitem4.setText("VALOR TOTAL");
        self.productTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)

        self.productTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        self.productTable.setColumnWidth(0, 70)  # coluna do código
        self.productTable.setColumnWidth(2, 115)  # coluna do preco un/kg
        self.productTable.setColumnWidth(3, 112)  # coluna do qtd/peso
        self.productTable.setColumnWidth(4, 112)  # coluna do valor total


    def removeProduct(self) -> None:
        selectedRow = self.productTable.currentRow()

        if selectedRow != -1:
            productNameSelected = self.productTable.item(selectedRow, 1).text()
            self.productTable.removeRow(selectedRow)
            self.allProductsAdded.remove(productNameSelected)
            print(f"produto removido e lista atual = {self.allProductsAdded}")

            # toda vez que um produto for removido é necessário somar novamente o valor total da venda
            self.sumTotalPrice()
        
        else:
            self.alerts.showAlert(3, "Selecione algum produto para remover.")


    def sumTotalPrice(self) -> None:
        totalPrice = 0
        rows = self.productTable.rowCount()
        for i in range(rows):
            totalProductValue = self.productTable.item(i, 4)
            totalProductValue = totalProductValue.text()
            totalProductValue = totalProductValue.replace("R$", "")
            totalPrice += float(totalProductValue)
        
        self.labelWithTotalSaleValue.setText(f"{totalPrice:.2f}")


    @close_connection
    def getComboBoxItems(self) -> Tuple[MySQLConnection, MySQLCursor]:
        self.conn = self.db.connectDb()
        self.cur = self.conn.cursor()

        selectQuery = (
            "SELECT name FROM payment_methods"
        )

        try:
            self.cur.execute(selectQuery)
        
        except (mysql.connector.Error) as err:
            self.alerts.showAlert(3, str(err))
        
        else:
            paymentMethodsList = self.cur.fetchall()

            for payment in paymentMethodsList:
                self.paymentMethodsComboBox.addItems(payment)

        return self.conn, self.cur


    def enabledDisabledLineEdit(self) -> None:
        currentPaymentMethod = self.paymentMethodsComboBox.currentText()
        self.installmentsLineEdit.setDisabled(True)

        if currentPaymentMethod == "credito parcelado":
            self.installmentsLineEdit.setDisabled(False)
    

    def getReceivedAndRemainingValue(self) -> float:
        currentRemainingValue = float(self.labelRemainingAmountToReceiveValue.text())
        currentTotalReceivedValue = float(self.labelTotalReceivedLabel.text())

        return currentRemainingValue, currentTotalReceivedValue


    def addPaymentMethod(self) -> None:
        if self.labelWithTotalSaleValue.text():
            # verificando se foi inserido um valor válido
            userValueInput = self.valueLineEdit.text()

            try:
                if "," in userValueInput:
                    userValueInput = userValueInput.replace(",", ".")
                
                userValueInput = float(userValueInput)

                if userValueInput == 0:
                    raise CannotBeZero
                elif userValueInput < 0:
                    raise CannotBeNegative
            
            except (ValueError, CannotBeNegative, CannotBeZero) as err:
                self.alerts.showAlert(3, "O valor de pagamento inserido é inválido.")
            
            else:
                # vamos detectar qual forma de pagamento foi selecionado
                currentPaymentMethod = self.paymentMethodsComboBox.currentText()

                if currentPaymentMethod in ["credito", "debito", "pix", "credito parcelado"]:
                    # vamos pegar o valor restante a pagar e o valor total
                    currentRemainingValue, currentTotalReceivedValue = self.getReceivedAndRemainingValue()

                    # pegando o valor do usuario
                    userInputValue = self.valueLineEdit.text()

                    if "," in userInputValue:
                        userInputValue = userInputValue.replace("," , ".")
                    
                    userInputValue = float(userInputValue)

                    # como o pagamento não é em dinheiro o valor pago não pode ser maior que o valor restante
                    if userInputValue > currentRemainingValue:
                        self.alerts.showAlert(3, "O valor inserido é maior do que o valor restante a pagar")

                    elif userInputValue == currentRemainingValue:
                        currentTotalReceivedValue += userInputValue  # somando o total recebido com o valor inserido
                        currentRemainingValue -= userInputValue  # subtraindo o valor inserido com o valor restante

                        self.updatePaymentsValue(currentRemainingValue, currentTotalReceivedValue)

                        # verificando sempre se o valor total foi pago já e chamando a funcao de finalizar
                        self.checkPayments()
                    
                    else:  # caso o pagamento seja menor que o valor restante
                        currentTotalReceivedValue += userInputValue
                        currentRemainingValue -= userInputValue

                        self.updatePaymentsValue(currentRemainingValue, currentTotalReceivedValue)

                        self.checkPayments()
                    
                    self.valueLineEdit.clear()


                else:  # se for no dinheiro
                    currentRemainingValue, currentTotalReceivedValue = self.getReceivedAndRemainingValue()
                    userInputValue = self.valueLineEdit.text()

                    if "," in userInputValue:
                        userInputValue = userInputValue.replace("," , ".")
                    
                    userInputValue = float(userInputValue)

                    if userInputValue > currentRemainingValue:
                        # se o valor inserido for maior, precisa ter troco
                        changeValue = 0

                        changeValue = userInputValue - currentRemainingValue
                        currentTotalReceivedValue += userInputValue
                        currentRemainingValue = 0

                        self.updatePaymentsValue(currentRemainingValue, currentTotalReceivedValue)
                        self.labelWithChangeValue.setText(f"{changeValue:.2f}")

                        self.checkPayments()

                    
                    else:
                        currentTotalReceivedValue += userInputValue
                        currentRemainingValue -= userInputValue

                        self.updatePaymentsValue(currentRemainingValue, currentTotalReceivedValue)

                        self.checkPayments()
                    
                    self.valueLineEdit.clear()
        
        else:
            self.alerts.showAlert(3, "Não é possível adicionar forma de pagamento, pois não há produto na venda.")


    def checkPayments(self) -> None:
        remainingValue = float(self.labelRemainingAmountToReceiveValue.text())
        changeValue = self.labelWithChangeValue.text()

        if remainingValue == 0:
            self.finishSale()
        # se o troco estiver com valor é porque chegou ao final da compra
        elif self.labelWithChangeValue.text():
            self.finishSale()
        else:
            pass


    def hiddenShowWidget(self, type: str) -> None:
        match type:
            case "notPay":
                self.addPaymentMethodButton.setHidden(True)
                self.valueLineEdit.setDisabled(True)
                self.deletePaymentMethods.setHidden(True)
                self.codeLineEdit.setDisabled(False)
                self.removeProductButton.setHidden(False)
                self.payButton.setHidden(False)

                # por enquanto
                self.installmentsLineEdit.setHidden(True)
                self.labelInstallments.setHidden(True)

            case "pay":
                self.addPaymentMethodButton.setHidden(False)
                self.valueLineEdit.setDisabled(False)
                self.deletePaymentMethods.setHidden(False)
                self.codeLineEdit.setDisabled(True)
                self.removeProductButton.setHidden(True)
            
            case "paying":
                self.payButton.setHidden(True)
            

    def paySale(self) -> None:
        if self.labelWithTotalSaleValue.text() == "":
            self.alerts.showAlert(3, "Adicione ao menos um produto na venda.")
        else:
            self.hiddenShowWidget("pay")
            self.hiddenShowWidget("paying")

            # definindo o total recebido e o valor restante inicial
            # total restante
            self.remainingValue = float(self.labelWithTotalSaleValue.text())
            self.labelRemainingAmountToReceiveValue.setText(f"{self.remainingValue:.2f}")

            # total recebido
            self.labelTotalReceivedLabel.setText("0.00")


    def deletePayment(self) -> None:
        self.hiddenShowWidget("notPay")
        self.remainingValue = float(self.labelWithTotalSaleValue.text())
        self.labelRemainingAmountToReceiveValue.setText(f"{self.remainingValue:.2f}")

        # total recebido
        self.labelTotalReceivedLabel.setText("0.00")

        # limpando os campos
        self.valueLineEdit.clear()
        self.installmentsLineEdit.clear()
        self.labelRemainingAmountToReceiveValue.clear()
        self.labelWithChangeValue.clear()


    def updatePaymentsValue(self, currentRemainingValue: float, currentReceivedValue: float) -> None:
        self.labelRemainingAmountToReceiveValue.setText(f"{currentRemainingValue:.2f}")
        self.labelTotalReceivedLabel.setText(f"{currentReceivedValue:.2f}")


    @close_connection
    def finishSale(self) -> Tuple[MySQLConnection, MySQLCursor]:
        self.conn = self.db.connectDb()
        self.cur = self.conn.cursor()
        
        self.alerts.showAlert(4)

        if self.alerts.msgConfirm.clickedButton() == self.alerts.buttonSim:
            total_sale_value = float(self.labelWithTotalSaleValue.text())

            change_value = 0
            if self.labelWithChangeValue.text() == "":
                change_value = 0
            else:
                change_value = float(self.labelWithChangeValue.text())

            customer_value_paid = str(self.labelTotalReceivedLabel.text())

            insertSaleQuery = (
                "INSERT INTO sales (sale_date, total_sale_value, change_value, customer_value_paid)\n"
                f"VALUES (CURRENT_DATE, {total_sale_value}, {change_value}, {customer_value_paid})"
            )

            rows = self.productTable.rowCount()

            insertSaleProductQuery = (
                "INSERT INTO sale_product (quantity_product, id_product, id_sale)\n"
                "VALUES (%s, %s, %s)"
            )

            try:
                self.cur.execute(insertSaleQuery)
                self.conn.commit()

                for i in range(rows):
                    productId = int(self.productTable.item(i, 0).text())
                    idSale = int(self.saleNumberLabel.text())
                    quantityProduct = self.productTable.item(i, 3).text()
                    if "gr" in quantityProduct:

                        quantityProduct = quantityProduct.replace("gr", "")
                        quantityProduct = float(quantityProduct)
                    
                    elif "un" in quantityProduct:
                        quantityProduct = quantityProduct.replace("un", "")
                        quantityProduct = float(quantityProduct)
                    
                    print(f"{rows=}")
                    print(f"{quantityProduct=}")

                    valuesToAdd = (quantityProduct, productId, idSale)
                    self.cur.execute(insertSaleProductQuery, valuesToAdd)
                    self.conn.commit()

            except (mysql.connector.Error) as err:
                self.alerts.showAlert(3, str(err))
            
            else:
                self.getNumberSale()

                self.alerts.showAlert(5, f"Venda Nº{idSale} foi registrada com sucesso.")

                self.productTable.setRowCount(0)
                self.allProductsAdded.clear()
                self.labelWithTotalSaleValue.clear()
                self.labelWithChangeValue.clear()
                self.labelTotalReceivedLabel.clear()
                self.hiddenShowWidget("notPay")

        else:
            pass
        
        return self.conn, self.cur


    @close_connection
    def getNumberSale(self) -> Tuple[MySQLConnection, MySQLCursor]:
        self.conn = self.db.connectDb()
        self.cur = self.conn.cursor()
        
        selectQuery = (
            "SELECT * FROM sales"
        )

        try:
            self.cur.execute(selectQuery)

        except (mysql.connector.Error) as err:
            self.alerts.showAlert(3, str(err))

        else:
            saleList = self.cur.fetchall()

            if self.cur.rowcount == 0:
                self.saleNumberLabel.setText("1")
            
            elif self.cur.rowcount > 0:
                saleVolume = len(saleList)

                saleNumber = saleVolume + 1

                print(f"{saleNumber=}")

                self.saleNumberLabel.setText(str(saleNumber))

        return self.conn, self.cur
