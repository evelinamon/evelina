import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication, QMessageBox, QComboBox)


class Pagrindinis_langas(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.formaLabel = QLabel(self)
        self.formaLabel.setText("Registracijos forma")
        self.formaLabel.move(100, 0)

        if self.comboBox() == 0:
            pass
        elif self.comboBox() == 1:
            self.comboBox().activated[str].connect(self.onChanged)

        else:
            self.nameLabel = QLabel(self)
            self.nameLabel.setText('Name:')
            self.line = QLineEdit(self)

            self.line.move(80, 100)
            self.line.resize(200, 32)
            self.nameLabel.move(20, 100)

            vardas = QLabel('Vardas')
            pavarde = QLabel('Pavarde')

            vardasEdit = QLineEdit()
            pavardeEdit = QLineEdit()

            grid = QGridLayout()
            grid.setSpacing(10)

            grid.addWidget(vardas, 1, 0)
            grid.addWidget(vardasEdit, 1, 1)

            grid.addWidget(pavarde, 2, 0)
            grid.addWidget(pavardeEdit, 2, 1, 1, 1)

            self.setLayout(grid)



        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Fakultetas')
        self.show()

    def comboBox(self):
        combo = QComboBox(self)
        combo.addItem("---")
        combo.addItem("Studentai")
        combo.addItem("Destytojai")
        combo.move(97, 40)

        #self.qlabel = QLabel(self)
        #self.qlabel.move(10, 70)


        combo.activated[str].connect(self.onChanged)
        index = combo.currentIndex()
        return index

    def onChanged(self):
        self.qlabel.setText("Studiju programa")
        self.qlabel.adjustSize()
        self.qline = QLineEdit(self)
        self.qline.move(100, 70)
        #self.qline.setText("labas")
        #self.qline.adjustSize()

    def onChanged1(self):
        self.qlabel.setText("Pareiga")
        self.qlabel.adjustSize()

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
