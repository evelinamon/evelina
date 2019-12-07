import sys
from PyQt5.QtWidgets import QApplication, QWidget,  QTabWidget, QGridLayout, \
    QMessageBox, QLabel, QLineEdit, QGroupBox, QVBoxLayout, QPushButton

class Pagrindinis_langas(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        tabs = QTabWidget()
        tabs.addTab(self.createStudentTab(), "Studentas")
        tabs.addTab(self.createLecturerTab(), "Destytojas")
        layout.addWidget(tabs)
        self.setLayout(layout)

        self.show()

    def createStudentTab(self):
        horizontalGroupBox = QGroupBox()
        groupBoxLayout = QGridLayout()
        groupBoxLayout.setColumnStretch(0, 1)
        groupBoxLayout.setColumnStretch(1, 2)

        groupBoxLayout.addWidget(QLabel("Vardas"), 0, 0)
        groupBoxLayout.addWidget(QLabel("Pavardė"), 1, 0)
        groupBoxLayout.addWidget(QLabel("Studijų programa"), 2, 0)
        groupBoxLayout.addWidget(QLabel("Kursas"), 3, 0)
        groupBoxLayout.addWidget(QLineEdit(), 0, 1)
        groupBoxLayout.addWidget(QLineEdit(), 1, 1)
        groupBoxLayout.addWidget(QLineEdit(), 2, 1)
        groupBoxLayout.addWidget(QLineEdit(), 3, 1)
        groupBoxLayout.addWidget(QPushButton("Įrašyti studentą"), 4, 0)

        horizontalGroupBox.setLayout(groupBoxLayout)

        return horizontalGroupBox

    def createLecturerTab(self):
        horizontalGroupBox = QGroupBox("")
        groupBoxLayout = QGridLayout()
        groupBoxLayout.setColumnStretch(0, 1)
        groupBoxLayout.setColumnStretch(1, 2)

        groupBoxLayout.addWidget(QLabel("Vardas"), 0, 0)
        groupBoxLayout.addWidget(QLabel("Pavardė"), 1, 0)
        groupBoxLayout.addWidget(QLabel("Pareiga"), 2, 0)
        groupBoxLayout.addWidget(QLabel("Kada pradėjo dirbti"), 3, 0)
        groupBoxLayout.addWidget(QLineEdit(), 0, 1)
        groupBoxLayout.addWidget(QLineEdit(), 1, 1)
        groupBoxLayout.addWidget(QLineEdit(), 2, 1)
        groupBoxLayout.addWidget(QLineEdit(), 3, 1)
        groupBoxLayout.addWidget(QPushButton("Įrašyti dėstytoją"), 4, 0)

        horizontalGroupBox.setLayout(groupBoxLayout)

        return horizontalGroupBox


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
