# main.py

import sys
from PyQt6.QtWidgets import QApplication
from image_processing.controller import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show()
    sys.exit(app.exec())
