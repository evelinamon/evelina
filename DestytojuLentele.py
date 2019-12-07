from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QMessageBox

class Issokantis_langas2(QWidget):

    def __init__(self, destytojai, fakultetas):
        super().__init__()
        self.setGeometry(300, 300, 480, 400)
        self.setWindowTitle("Dėstytojų sąrašas")
        self.sarasas = destytojai.values()
        self.fakultetas = fakultetas
        self.tableWidget = QTableWidget()
        self.createTable()
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.show()

    def createTable(self):
        self.tableWidget.setRowCount(len(self.sarasas))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Vardas", "Pavarde", "Pareiga", "Nuo kada dirba"])

        row = 0
        for destytojas in self.sarasas:
            column = 0
            self.tableWidget.setItem(row, column, QTableWidgetItem(destytojas.gauti_varda()))
            self.tableWidget.setItem(row, column + 1, QTableWidgetItem(destytojas.gauti_pavarde()))
            self.tableWidget.setItem(row, column + 2, QTableWidgetItem(destytojas.pareiga))
            self.tableWidget.setItem(row, column + 3, QTableWidgetItem(destytojas.kada_pradejo))
            row = row + 1
        self.tableWidget.cellDoubleClicked.connect(self.on_double_clicked)

    def on_double_clicked(self, row):
        vardas = self.tableWidget.item(row, 0).text()
        self.istrintiEvent(vardas, row)

    def istrintiEvent(self, vardas, row):
        reply = QMessageBox.question(self, 'Message',
                                     "Ar tikrai norite istrinti?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.fakultetas.istrinti_destytojus(vardas)
            self.tableWidget.removeRow(row)