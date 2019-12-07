from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QMessageBox

class Issokantis_langas(QWidget):

    def __init__(self, studentai, fakultetas):
        """Konstruktorius"""
        super().__init__()
        self.setGeometry(300, 300, 425, 400)
        self.setWindowTitle("Studentų sąrašas")
        self.sarasas = studentai.values()
        self.fakultetas = fakultetas
        self.tableWidget = QTableWidget()
        self.fillTable()
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.show()

    def fillTable(self):
        """Uzpildo lentele"""
        self.tableWidget.setRowCount(len(self.sarasas))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Vardas", "Pavarde", "Studiju programa", "Kursas"])

        row = 0
        for studentas in self.sarasas:
            column = 0
            self.tableWidget.setItem(row, column, QTableWidgetItem(studentas.gauti_varda()))
            self.tableWidget.setItem(row, column + 1, QTableWidgetItem(studentas.gauti_pavarde()))
            self.tableWidget.setItem(row, column + 2, QTableWidgetItem(studentas.studiju_programa))
            self.tableWidget.setItem(row, column + 3, QTableWidgetItem(studentas.kursas))
            row = row + 1
        self.tableWidget.cellDoubleClicked.connect(self.on_double_clicked)

    def on_double_clicked(self, row):
        """Dvigubas paspaudimas istrina studenta"""
        vardas = self.tableWidget.item(row, 0).text()
        self.istrintiEvent(vardas, row)


    def istrintiEvent(self, vardas, row):
        """Informacinis langas"""
        reply = QMessageBox.question(self, 'Message',
                                     "Ar tikrai norite istrinti?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.fakultetas.istrinti_studenta(vardas)
            self.tableWidget.removeRow(row)
