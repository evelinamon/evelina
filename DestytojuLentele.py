from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QMessageBox

class Issokantislangas2(QWidget):
    """Issokancio lango 2 klase"""

    def __init__(self, destytojai, fakultetas):
        """Konstruktorius"""
        super().__init__()
        self.setGeometry(300, 300, 480, 400)
        self.setWindowTitle("Dėstytojų sąrašas")
        self.sarasas = destytojai.values()
        self.fakultetas = fakultetas
        self.tablewidget = QTableWidget()
        self.filltable()
        layout = QVBoxLayout()
        layout.addWidget(self.tablewidget)
        self.setLayout(layout)

        self.show()

    def filltable(self):
        """Uzpildo lentele"""
        self.tablewidget.setRowCount(len(self.sarasas))
        self.tablewidget.setColumnCount(4)
        self.tablewidget.setHorizontalHeaderLabels(["Vardas", "Pavarde", "Pareiga", "Nuo kada dirba"])

        row = 0
        for destytojas in self.sarasas:
            column = 0
            self.tablewidget.setItem(row, column, QTableWidgetItem(destytojas.gauti_varda()))
            self.tablewidget.setItem(row, column + 1, QTableWidgetItem(destytojas.gauti_pavarde()))
            self.tablewidget.setItem(row, column + 2, QTableWidgetItem(destytojas.pareiga))
            self.tablewidget.setItem(row, column + 3, QTableWidgetItem(destytojas.kada_pradejo))
            row = row + 1
        self.tablewidget.cellDoubleClicked.connect(self.on_double_clicked)

    def on_double_clicked(self, row):
        """Dvigubas paspaudimas istrina destytoja"""
        vardas = self.tablewidget.item(row, 0).text()
        self.istrinti_event(vardas, row)

    def istrinti_event(self, vardas, row):
        """Informacine zinute"""
        reply = QMessageBox.question(self, 'Message',
                                     "Ar tikrai norite istrinti?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.fakultetas.istrinti_destytojus(vardas)
            self.tablewidget.removeRow(row)