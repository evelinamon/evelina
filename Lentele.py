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

        vardas = ""
        for kopustas in self.sarasas:
            vardas = kopustas.gauti_varda()

        self.tableWidget.setItem(0, 0, QTableWidgetItem(vardas))
        self.tableWidget.setItem(0, 1, QTableWidgetItem())
        self.tableWidget.setItem(1, 0, QTableWidgetItem())
        self.tableWidget.setItem(1, 1, QTableWidgetItem())
        self.tableWidget.setItem(2, 0, QTableWidgetItem())
        self.tableWidget.setItem(2, 1, QTableWidgetItem())
        self.tableWidget.setItem(3, 0, QTableWidgetItem())
        self.tableWidget.setItem(3, 1, QTableWidgetItem())
        self.tableWidget.move(0, 0)