import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, \
    QMessageBox, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class Pagrindinis_langas(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.show()

class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "Studentai")
        self.tabs.addTab(self.tab2, "Destytojai")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.vardasLabel = QLabel(self)
        self.vardasLabel.setText("Vardas")
        self.vardasLabel.move(10, 70)
        self.pavardeLabel = QLabel(self)
        self.pavardeLabel.setText("Pavarde")
        self.pavardeLabel.move(10, 100)
        self.vardasLine = QLineEdit(self)
        self.vardasLine.move(100, 70)
        self.vardasLine.adjustSize()
        self.tab1.layout.addWidget(self.vardasLabel)
        self.tab1.layout.addWidget(self.pavardeLabel)
        self.tab1.layout.addWidget(self.vardasLine)
        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

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
