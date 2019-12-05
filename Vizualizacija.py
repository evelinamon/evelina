import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication, QMessageBox, QComboBox)


class Pagrindinis_langas(QWidget):

    def __init__(self):
        super().__init__()

        self.qlabel = QLabel(self)
        self.comboBox = self.createComboBox()
        self.formaLabel = QLabel(self)
        self.initUI()

    def initUI(self):

        self.formaLabel.setText("Registracijos forma")
        self.formaLabel.move(100, 0)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Fakultetas')
        self.show()

    def createComboBox(self):
        combo = QComboBox(self)
        combo.addItem("---")
        combo.addItem("Studentai")
        combo.addItem("Destytojai")
        combo.move(97, 40)

        combo.activated[str].connect(self.onChanged)
        return combo
    def onChanged(self):
        self.qlabel.move(10, 70)
        if self.comboBox.currentIndex() == 0:
            pass
        elif self.comboBox.currentIndex() == 1:
            self.qlabel.setText("Studiju programa")
            self.qlabel.adjustSize()
            return self.qlabel
        else:
            self.qlabel.setText("Pareiga")
            self.qlabel.adjustSize()
            return self.qlabel



            #self.qline = QLineEdit(self)
            #self.qline.move(100, 70)
            #self.qline.setText("labas")
            #self.qline.adjustSize()0

    """def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pagrindinis_langas()
    sys.exit(app.exec_())
