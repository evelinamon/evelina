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
        pavarde = ""
        studiju_programa = ""
        kursas = ""
        row = 0
        column = 0

        for studentai in self.sarasas:
            vardas = studentai.gauti_varda()
            pavarde = studentai.gauti_pavarde()
            studiju_programa = studentai.studiju_programa
            kursas = studentai.kursas
            for elementai in range(4, 0, -1):
                row = row + 1
                column = 0

        self.tableWidget.setItem(row, column, QTableWidgetItem(vardas))
        self.tableWidget.setItem(row, column+1, QTableWidgetItem(pavarde))
        self.tableWidget.setItem(row, column+2, QTableWidgetItem(studiju_programa))
        self.tableWidget.setItem(row, column+3, QTableWidgetItem(kursas))
        self.tableWidget.move(0, 0)