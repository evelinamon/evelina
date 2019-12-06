import sys
from PyQt5.QtWidgets import QApplication, QWidget,  QTabWidget, QGridLayout, \
    QMessageBox, QLabel, QLineEdit, QGroupBox, QVBoxLayout

class Pagrindinis_langas(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        tabs = QTabWidget()
        tabs.addTab(self.createStudentTab(), "Studentas")
        layout.addWidget(tabs)
        self.setLayout(layout)

        self.show()

    def createStudentTab(self):
        horizontalGroupBox = QGroupBox()
        groupBoxLayout = QGridLayout()
        groupBoxLayout.setColumnStretch(0, 1)
        groupBoxLayout.setColumnStretch(1, 2)

        groupBoxLayout.addWidget(QLabel("Vardas"), 0, 0)
        groupBoxLayout.addWidget(QLabel("Pavarde"), 1, 0)
        groupBoxLayout.addWidget(QLabel("Studiju programa"), 2, 0)
        groupBoxLayout.addWidget(QLabel("Kursas"), 3, 0)
        groupBoxLayout.addWidget(QLineEdit(), 0, 1)
        groupBoxLayout.addWidget(QLineEdit(), 1, 1)
        groupBoxLayout.addWidget(QLineEdit(), 2, 1)
        groupBoxLayout.addWidget(QLineEdit(), 3, 1)

        horizontalGroupBox.setLayout(groupBoxLayout)

        return horizontalGroupBox

    def createGridLayout2(self):
        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 2)

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
        layout.addWidget(self.vardasLabel, 0, 0)
        layout.addWidget(self.pavardeLabel, 1, 0)
        layout.addWidget(self.pareigaLabel, 2, 0)
        layout.addWidget(self.vardasLine, 0, 1)
        layout.addWidget(self.pavardeLine, 1, 1)
        layout.addWidget(self.pareigaLine, 2, 1)

        self.horizontalGroupBox.setLayout(layout)


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
