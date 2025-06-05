# main.py

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget
from image_processing.vue_retrait_radient import RetraitRadient


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AstroRatio")
        # self.resize(1000, 600)
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.retrait_radient = RetraitRadient(self)
        self.tab_widget.addTab(self.retrait_radient, "Retrait du radiant")
        # self.tab_widget.addTab(DifferentRadient(), "Différents types de radiants")

        ###### Menu ######

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("Fichier")

        # self.open_action = self.file_menu.addAction("Ouvrir une image")
        # # self.open_action.triggered.connect(self.controller.choose_image)
        # self.open_action.setShortcut("Ctrl+O")

        # self.open_folder_action = self.file_menu.addAction("Ouvrir un dossier")
        # self.open_folder_action.triggered.connect(
        #     self.retrait_radient.controller.select_folder
        # )
        # self.open_folder_action.setShortcut("Ctrl+Shift+O")

        self.file_menu.addSeparator()

        self.save_action = self.file_menu.addAction("Sauvegarder le résultat")
        self.save_action.triggered.connect(lambda x: x)
        # TODO - Sauvegarde des fichiers
        self.save_action.setShortcut("Ctrl+S")

        self.process_menu = self.menu.addMenu("Calcul")
        self.process_action = self.process_menu.addAction("Calculer actuel")
        self.process_action.triggered.connect(
            self.retrait_radient.pipeline.process_selected_step
        )
        self.process_action.setShortcut("Ctrl+R")

        self.process_all_action = self.process_menu.addAction("Calculer tout")
        self.process_all_action.triggered.connect(
            self.retrait_radient.pipeline.process_all
        )
        self.process_all_action.setShortcut("Ctrl+Shift+R")

        # Calculer automatiquement
        self.process_menu.addSeparator()
        self.auto_process_action = self.process_menu.addAction(
            "Calculer au changement des paramètres"
        )
        self.auto_process_action.setCheckable(True)
        self.auto_process_action.triggered.connect(
            self.retrait_radient.pipeline.set_auto_process
        )
        self.auto_process_action.setShortcut("Ctrl+Alt+R")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Application = MainWindow()
    Application.show()
    sys.exit(app.exec())
