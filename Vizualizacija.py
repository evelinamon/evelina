import sys
from PyQt5.QtWidgets import QApplication, QWidget,  QTabWidget, QGridLayout, \
    QMessageBox, QLabel, QLineEdit, QGroupBox, QVBoxLayout, QPushButton
from Fakultetas import Fakultetas
from Lentele import Issokantis_langas

class Pagrindinis_langas(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        tabs = QTabWidget()
        self.vardasStudentoQLineEdit = QLineEdit()
        self.pavardeStudentoQLineEdit = QLineEdit()
        self.studiju_programaQLineEdit = QLineEdit()
        self.kursasQLineEdit = QLineEdit()
        self.vardasDestytojoQLineEdit = QLineEdit()
        self.pavardeDestytojoQLineEdit = QLineEdit()
        self.pareigaQLineEdit = QLineEdit()
        self.kada_pradejoQLineEdit = QLineEdit()
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
        irasyti_studentaButton.clicked.connect(self.on_clickStudentas)
        studentu_sarasasButton = QPushButton("Studentų sąrašas")
        studentu_sarasasButton.clicked.connect(self.on_click_studentu_sarasasButton)

        groupBoxLayout.setColumnStretch(0, 1)
        groupBoxLayout.setColumnStretch(1, 2)

        groupBoxLayout.addWidget(QLabel("Vardas"), 0, 0)
        groupBoxLayout.addWidget(QLabel("Pavardė"), 1, 0)
        groupBoxLayout.addWidget(QLabel("Studijų programa"), 2, 0)
        groupBoxLayout.addWidget(QLabel("Kursas"), 3, 0)
        groupBoxLayout.addWidget(self.vardasStudentoQLineEdit, 0, 1)
        groupBoxLayout.addWidget(self.pavardeStudentoQLineEdit, 1, 1)
        groupBoxLayout.addWidget(self.studiju_programaQLineEdit, 2, 1)
        groupBoxLayout.addWidget(self.kursasQLineEdit, 3, 1)
        groupBoxLayout.addWidget(irasyti_studentaButton, 4, 0)
        groupBoxLayout.addWidget(studentu_sarasasButton, 5, 0)

        horizontalGroupBox.setLayout(groupBoxLayout)

        return horizontalGroupBox

    def createLecturerTab(self):
        horizontalGroupBox = QGroupBox("")
        groupBoxLayout = QGridLayout()
        irasyti_destytojaButton = QPushButton("Įrašyti dėstytoją")
        irasyti_destytojaButton.clicked.connect(self.on_clickDestytojas)
        groupBoxLayout.setColumnStretch(0, 1)
        groupBoxLayout.setColumnStretch(1, 2)
        groupBoxLayout.addWidget(QLabel("Vardas"), 0, 0)
        groupBoxLayout.addWidget(QLabel("Pavardė"), 1, 0)
        groupBoxLayout.addWidget(QLabel("Pareiga"), 2, 0)
        groupBoxLayout.addWidget(QLabel("Kada pradėjo dirbti"), 3, 0)
        groupBoxLayout.addWidget(self.vardasDestytojoQLineEdit, 0, 1)
        groupBoxLayout.addWidget(self.pavardeDestytojoQLineEdit, 1, 1)
        groupBoxLayout.addWidget(self.pareigaQLineEdit, 2, 1)
        groupBoxLayout.addWidget(self.kada_pradejoQLineEdit, 3, 1)
        groupBoxLayout.addWidget(irasyti_destytojaButton, 4, 0)

        horizontalGroupBox.setLayout(groupBoxLayout)

        return horizontalGroupBox

    def on_clickStudentas(self):
        self.fakultetas.priimti_studenta(self.vardasStudentoQLineEdit.text(),
                                         self.pavardeStudentoQLineEdit.text(),
                                         self.studiju_programaQLineEdit.text(),
                                         self.kursasQLineEdit.text())

    def on_clickDestytojas(self):
        self.fakultetas.priimti_destytoja(self.vardasDestytojoQLineEdit.text(),
                                          self.pavardeDestytojoQLineEdit.text(),
                                          self.pareigaQLineEdit.text(),
                                          self.kada_pradejoQLineEdit.text())
    def on_click_studentu_sarasasButton(self):
        self.issokantis_langas = Issokantis_langas(self.fakultetas)


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
