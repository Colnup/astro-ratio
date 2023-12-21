# main.py

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget
from image_processing.controller import Controller
from image_processing.vue_retrait_radient import RetraitRadient
from image_processing.vue_type_radient import DifferentRadient


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = Controller()
        self.setWindowTitle("AstroRatio")
        self.resize(1000, 600)
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)
        self.tab_widget.addTab(RetraitRadient(), "Retrait du radiant")
        self.tab_widget.addTab(DifferentRadient(), "Différents types de radiants")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Application = MainWindow()
    Application.show()
    sys.exit(app.exec())
