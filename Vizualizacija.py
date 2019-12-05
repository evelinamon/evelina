import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QGridLayout, \
    QMessageBox, QLabel, QLineEdit, QGroupBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class Pagrindinis_langas(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 300
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.show()

class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.horizontalGroupBox = QGroupBox("Grid")
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)


        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "Studentai")
        self.tabs.addTab(self.tab2, "Destytojai")

        self.layout.setColumnStretch(1, 4)
        self.layout.setColumnStretch(2, 4)

        # Create first tab
        self.tab1.layout = QGridLayout(self)
        self.vardasLabel = QLabel(self)
        self.vardasLabel.setText("Vardas")
        self.pavardeLabel = QLabel(self)
        self.pavardeLabel.setText("Pavarde")
        self.studiju_programa_Label = QLabel(self)
        self.studiju_programa_Label.setText("Studiju programa")
        self.kursasLabel = QLabel(self)
        self.kursasLabel.setText("Kursas")
        self.vardasLine = QLineEdit(self)
        self.vardasLine.adjustSize()
        self.pavardeLine = QLineEdit(self)
        self.pavardeLine.adjustSize()
        self.studiju_programa_Line = QLineEdit(self)
        self.studiju_programa_Line.adjustSize()
        self.kursasLine = QLineEdit(self)
        self.kursasLine.adjustSize()
        self.tab1.layout.addWidget(self.vardasLabel, 0, 0)
        self.tab1.layout.addWidget(self.pavardeLabel, 1, 0)
        self.tab1.layout.addWidget(self.studiju_programa_Label, 2, 0)
        self.tab1.layout.addWidget(self.kursasLabel, 3, 0)
        self.tab1.layout.addWidget(self.vardasLine, 0, 1)
        self.tab1.layout.addWidget(self.pavardeLine, 1, 1)
        self.tab1.layout.addWidget(self.studiju_programa_Line, 2, 1)
        self.tab1.layout.addWidget(self.kursasLine, 3, 1)
        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)

        self.setWindowTitle('Fakultetas')
        self.show()


    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pagrindinis_langas()
    sys.exit(app.exec_())
