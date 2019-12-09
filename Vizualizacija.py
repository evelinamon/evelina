import sys
from PyQt5.QtWidgets import QApplication, QWidget,  QTabWidget, QGridLayout, \
    QMessageBox, QLabel, QLineEdit, QGroupBox, QVBoxLayout, QPushButton
from Fakultetas import Fakultetas
from StudentuLentele import Issokantislangas
from DestytojuLentele import Issokantislangas2

class Pagrindinis_langas(QWidget):
    """Pagrindinio lango klase"""

    def __init__(self):
        """Konstruktorius"""
        super().__init__()
        self.setWindowTitle("Fakultetas")
        layout = QVBoxLayout()
        tabs = QTabWidget()
        self.vardas_studento_q_line_edit = QLineEdit()
        self.pavarde_studento_q_line_edit = QLineEdit()
        self.studiju_programa_q_line_edit = QLineEdit()
        self.kursas_q_line_edit = QLineEdit()
        self.vardas_destytojo_q_line_edit = QLineEdit()
        self.pavarde_destytojo_q_line_edit = QLineEdit()
        self.pareiga_q_line_edit = QLineEdit()
        self.kada_pradejo_q_line_edit = QLineEdit()
        self.kiek_laiko_desto_q_line_edit = QLineEdit()
        tabs.addTab(self.fill_student_tab(), "Studentas")
        tabs.addTab(self.fill_lecturer_tab(), "Destytojas")
        layout.addWidget(tabs)
        self.setLayout(layout)
        self.fakultetas = Fakultetas("MIF", "Naugarduko 24")

        self.show()

    def fill_student_tab(self):
        """Uzpildo skirtuka"""
        horizontal_group_box = QGroupBox()
        group_box_layout = QGridLayout()
        irasyti_studenta_button = QPushButton("Įrašyti studentą")
        irasyti_studenta_button.clicked.connect(self.on_click_studentas)
        studentu_sarasas_button = QPushButton("Studentų sąrašas")
        studentu_sarasas_button.clicked.connect(self.on_click_studentu_sarasas_button)
        group_box_layout.setColumnStretch(0, 1)
        group_box_layout.setColumnStretch(1, 2)
        group_box_layout.addWidget(QLabel("Vardas"), 0, 0)
        group_box_layout.addWidget(QLabel("Pavardė"), 1, 0)
        group_box_layout.addWidget(QLabel("Studijų programa"), 2, 0)
        group_box_layout.addWidget(QLabel("Kursas"), 3, 0)
        group_box_layout.addWidget(self.vardas_studento_q_line_edit, 0, 1)
        group_box_layout.addWidget(self.pavarde_studento_q_line_edit, 1, 1)
        group_box_layout.addWidget(self.studiju_programa_q_line_edit, 2, 1)
        group_box_layout.addWidget(self.kursas_q_line_edit, 3, 1)
        group_box_layout.addWidget(irasyti_studenta_button, 4, 0)
        group_box_layout.addWidget(studentu_sarasas_button, 5, 0)
        horizontal_group_box.setLayout(group_box_layout)
        return horizontal_group_box

    def fill_lecturer_tab(self):
        """Uzpildo skituka"""
        horizontal_group_box = QGroupBox()
        group_box_layout = QGridLayout()
        irasyti_destytoja_button = QPushButton("Įrašyti dėstytoją")
        irasyti_destytoja_button.clicked.connect(self.on_click_destytojas)
        destytoju_sarasas_button = QPushButton("Dėstytojų sąrašas")
        destytoju_sarasas_button.clicked.connect(self.on_click_destytoju_sarasas_button)
        valandu_kiekis_button = QPushButton("Valandu kiekis")
        valandu_kiekis_button.clicked.connect(self.on_click_valandu_kiekis_button)
        group_box_layout.setColumnStretch(0, 1)
        group_box_layout.setColumnStretch(1, 2)
        group_box_layout.addWidget(QLabel("Vardas"), 0, 0)
        group_box_layout.addWidget(QLabel("Pavardė"), 1, 0)
        group_box_layout.addWidget(QLabel("Pareiga"), 2, 0)
        group_box_layout.addWidget(QLabel("Kada pradėjo dirbti"), 3, 0)
        group_box_layout.addWidget(QLabel("Kiek valandu desto"), 4, 0)
        group_box_layout.addWidget(self.vardas_destytojo_q_line_edit, 0, 1)
        group_box_layout.addWidget(self.pavarde_destytojo_q_line_edit, 1, 1)
        group_box_layout.addWidget(self.pareiga_q_line_edit, 2, 1)
        group_box_layout.addWidget(self.kada_pradejo_q_line_edit, 3, 1)
        group_box_layout.addWidget(self.kiek_laiko_desto_q_line_edit, 4, 1)
        group_box_layout.addWidget(irasyti_destytoja_button, 5, 0)
        group_box_layout.addWidget(destytoju_sarasas_button, 6, 0)
        group_box_layout.addWidget(valandu_kiekis_button, 7, 0)

        horizontal_group_box.setLayout(group_box_layout)

        return horizontal_group_box

    def on_click_studentas(self):
        """Mygtuko paspaudimas priima studenta"""
        self.fakultetas.priimti_studenta(self.vardas_studento_q_line_edit.text(),
                                         self.pavarde_studento_q_line_edit.text(),
                                         self.studiju_programa_q_line_edit.text(),
                                         self.kursas_q_line_edit.text())

    def on_click_destytojas(self):
        """Mygtuko paspaudimas priima destytoja"""
        self.fakultetas.priimti_destytoja(self.vardas_destytojo_q_line_edit.text(),
                                          self.pavarde_destytojo_q_line_edit.text(),
                                          self.pareiga_q_line_edit.text(),
                                          self.kada_pradejo_q_line_edit.text(),
                                          self.kiek_laiko_desto_q_line_edit.text())

    def on_click_studentu_sarasas_button(self):
        """Atidaro Issokanti langa"""
        self.issokantis_langas = Issokantislangas(self.fakultetas.studentai, self.fakultetas)

    def on_click_destytoju_sarasas_button(self):
        """Atidaro Issokantis langas 2"""
        self.issokantis_langas2 = Issokantislangas2(self.fakultetas.destytojai, self.fakultetas)

    def on_click_valandu_kiekis_button(self):
        """Mygtuko paspaudimas apskaiciuoja destytoju destomu valandu skaiciu"""
        QMessageBox.about(self, "Kiek valandu desto", "Desto: {}".format(str(self.fakultetas.desto_valandu())))

    def closeEvent(self, event):
        """Informacine zinute"""
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


app = QApplication(sys.argv)
ex = Pagrindinis_langas()
sys.exit(app.exec_())
