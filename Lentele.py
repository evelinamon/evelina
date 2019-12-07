import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Issokantis_langas(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Studentų sąrašas")

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Issokantis_langas()
    sys.exit(app.exec_())