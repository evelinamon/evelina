import sys
from PyQt5.QtWidgets import QApplication, QWidget,  QTabWidget, QGridLayout, \
    QMessageBox, QLabel, QLineEdit, QGroupBox, QVBoxLayout, QPushButton
from Fakultetas import Fakultetas

class Pagrindinis_langas(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        tabs = QTabWidget()
        self.vardasQLineEdit = QLineEdit()
        self.pavardeQLineEdit = QLineEdit()
        self.studiju_programaQLineEdit = QLineEdit()
        self.kursasQLineEdit = QLineEdit()
        tabs.addTab(self.createStudentTab(), "Studentas")
        tabs.addTab(self.createLecturerTab(), "Destytojas")
        layout.addWidget(tabs)
        self.setLayout(layout)
        self.fakultetas = Fakultetas("MIF", "Naugarduko 24")

        self.show()

    def createStudentTab(self):
        horizontalGroupBox = QGroupBox()
        groupBoxLayout = QGridLayout()
        irasyti_studentaButton = QPushButton("Įrašyti studentą")
        groupBoxLayout.setColumnStretch(0, 1)
        groupBoxLayout.setColumnStretch(1, 2)

        groupBoxLayout.addWidget(QLabel("Vardas"), 0, 0)
        groupBoxLayout.addWidget(QLabel("Pavardė"), 1, 0)
        groupBoxLayout.addWidget(QLabel("Studijų programa"), 2, 0)
        groupBoxLayout.addWidget(QLabel("Kursas"), 3, 0)
        groupBoxLayout.addWidget(self.vardasQLineEdit, 0, 1)
        groupBoxLayout.addWidget(self.pavardeQLineEdit, 1, 1)
        groupBoxLayout.addWidget(self.studiju_programaQLineEdit, 2, 1)
        groupBoxLayout.addWidget(self.kursasQLineEdit, 3, 1)
        groupBoxLayout.addWidget(irasyti_studentaButton, 4, 0)

        irasyti_studentaButton.clicked.connect(self.on_click)

        horizontalGroupBox.setLayout(groupBoxLayout)

        return horizontalGroupBox

    def createLecturerTab(self):
        horizontalGroupBox = QGroupBox("")
        groupBoxLayout = QGridLayout()
        vardasQLineEdit = QLineEdit()
        pavardeQLineEdit = QLineEdit()
        pareigaQLineEdit = QLineEdit()
        kada_pradejo_dirbtiQLineEdit = QLineEdit()
        groupBoxLayout.setColumnStretch(0, 1)
        groupBoxLayout.setColumnStretch(1, 2)

        groupBoxLayout.addWidget(QLabel("Vardas"), 0, 0)
        groupBoxLayout.addWidget(QLabel("Pavardė"), 1, 0)
        groupBoxLayout.addWidget(QLabel("Pareiga"), 2, 0)
        groupBoxLayout.addWidget(QLabel("Kada pradėjo dirbti"), 3, 0)
        groupBoxLayout.addWidget(vardasQLineEdit, 0, 1)
        groupBoxLayout.addWidget(pavardeQLineEdit, 1, 1)
        groupBoxLayout.addWidget(pareigaQLineEdit, 2, 1)
        groupBoxLayout.addWidget(kada_pradejo_dirbtiQLineEdit, 3, 1)
        groupBoxLayout.addWidget(QPushButton("Įrašyti dėstytoją"), 4, 0)

        horizontalGroupBox.setLayout(groupBoxLayout)

        return horizontalGroupBox

    def on_click(self):
        self.fakultetas.priimti_studenta(self.vardasQLineEdit.text(), self.pavardeQLineEdit.text(), self.studiju_programaQLineEdit.text(), self.kursasQLineEdit.text())

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
