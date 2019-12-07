import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from Fakultetas import Fakultetas

class Issokantis_langas(QWidget):

    def __init__(self, fakultetas):
        super().__init__()
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Studentų sąrašas")
        self.tableWidget = QTableWidget()
        self.createTable()
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)
        self.fakultetas = fakultetas
        self.sarasas = self.fakultetas.gauti_studentu_sarasa().values()
        self.show()

    def createTable(self):

        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Vardas", "Pavarde", "Studiju programa", "Kursas"])
        self.tableWidget.setItem(0, 0, QTableWidgetItem(self.sarasas[0].gauti_varda()))
        self.tableWidget.setItem(0, 1, QTableWidgetItem())
        self.tableWidget.setItem(1, 0, QTableWidgetItem())
        self.tableWidget.setItem(1, 1, QTableWidgetItem())
        self.tableWidget.setItem(2, 0, QTableWidgetItem())
        self.tableWidget.setItem(2, 1, QTableWidgetItem())
        self.tableWidget.setItem(3, 0, QTableWidgetItem())
        self.tableWidget.setItem(3, 1, QTableWidgetItem())
        self.tableWidget.move(0, 0)