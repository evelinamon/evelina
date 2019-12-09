import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QLabel


class Pagrindinis_langas(QWidget):
    """Pagrindinio lango klase"""

    def __init__(self):
        """Konstruktorius"""
        super().__init__()
        self.setGeometry(300, 300, 100, 100)
        self.setWindowTitle("Fakultetas")
        layout = QVBoxLayout()
        layout.addWidget(QLabel({}))

        self.show()


app = QApplication(sys.argv)
ex = Pagrindinis_langas()
sys.exit(app.exec_())