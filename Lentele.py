import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from Fakultetas import Fakultetas

class Issokantis_langas(QWidget):

    def __init__(self, studentai):
        super().__init__()
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Studentų sąrašas")
        self.sarasas = studentai.values()
        self.tableWidget = QTableWidget()
        self.createTable()
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.show()

    def createTable(self):
        self.tableWidget.setRowCount(4)
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
        self.tableWidget.move(0, 0)

    def on_double_clicked(self, a, b):
        self.tableWidget.removeRow(a)