import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QGridLayout, \
    QMessageBox, QLabel, QLineEdit, QGroupBox, QDialog, QVBoxLayout
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

class MyTableWidget(QDialog):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        #self.tabs.resize(300, 300)

        # Add tabs
        self.tabs.addTab(self.tab1, "Studentai")
        self.tabs.addTab(self.tab2, "Destytojai")

        self.createGridLayout()


        self.tab1Layout = QVBoxLayout()
        self.tab1Layout.addWidget(self.horizontalGroupBox)
        self.setLayout(self.tab1Layout)




        self.tab2.layout = QGridLayout(self)
        """
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
        """
        #self.tab1.setLayout(self.tab1.layout)

        self.vardasLabel = QLabel(self)
        self.vardasLabel.setText("Vardas")
        self.pavardeLabel = QLabel(self)
        self.pavardeLabel.setText("Pavarde")
        self.vardasLine = QLineEdit(self)
        self.vardasLine.adjustSize()
        self.pavardeLine = QLineEdit(self)
        self.pavardeLine.adjustSize()
        self.pareigaLabel = QLabel(self)
        self.pareigaLabel.setText("Pareiga")
        self.pareigaLine = QLineEdit(self)
        self.pareigaLine.adjustSize()
        self.tab2.layout.addWidget(self.vardasLabel, 0, 0)
        self.tab2.layout.addWidget(self.pavardeLabel, 1, 0)
        self.tab2.layout.addWidget(self.pareigaLabel, 2, 0)
        self.tab2.layout.addWidget(self.vardasLine, 0, 1)
        self.tab2.layout.addWidget(self.pavardeLine, 1, 1)
        self.tab2.layout.addWidget(self.pareigaLine, 2, 1)
        self.tab2.setLayout(self.tab2.layout)

        #self.pybutton = QPushButton('Įrašyti studentą', self)
        #self.pybutton.clicked.connect(self.clickMethod)
        #self.tab1.layout.addWidget(self.pybutton, 4, 0)

        self.setWindowTitle('Fakultetas')
        self.show()

    def clickMethod(self):
        self.vardasLineValue = self.vardasLine.text()
        QMessageBox.question(self, 'Studentas', "You typed: " + self.vardasLineValue, QMessageBox.Ok,
                             QMessageBox.Ok)
        self.vardasLine.setText("")

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 2)

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
        layout.addWidget(self.vardasLabel, 0, 0)
        layout.addWidget(self.pavardeLabel, 1, 0)
        layout.addWidget(self.studiju_programa_Label, 2, 0)
        layout.addWidget(self.kursasLabel, 3, 0)
        layout.addWidget(self.vardasLine, 0, 1)
        layout.addWidget(self.pavardeLine, 1, 1)
        layout.addWidget(self.studiju_programa_Line, 2, 1)
        layout.addWidget(self.kursasLine, 3, 1)

        self.horizontalGroupBox.setLayout(layout)

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
