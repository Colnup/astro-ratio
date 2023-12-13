# view.py

from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QLabel,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage


class MainUI(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Retirer Gradient")  # Appel correct de setWindowTitle
        self.resize(1200, 800)

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        # Layout principal (vertical)
        mainLayout = QVBoxLayout(centralWidget)

        # QLabel pour l'image
        self.imageLabel = QLabel()
        self.imageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainLayout.addWidget(self.imageLabel)

        # Layout pour les boutons (horizontal)
        buttonsLayout = QHBoxLayout()

        # Bouton 'Ouvrir Image'
        self.btnOpen = QPushButton("Ouvrir Image")
        self.btnOpen.clicked.connect(self.openImage)
        buttonsLayout.addWidget(self.btnOpen)

        # Bouton 'Retirer Gradient'
        self.btnRemoveGradient = QPushButton("Retirer Gradient")
        self.btnRemoveGradient.clicked.connect(self.controller.removeGradient)
        buttonsLayout.addWidget(self.btnRemoveGradient)

        # Ajouter un espace de chaque côté pour centrer les boutons
        buttonsLayout.addStretch()
        buttonsLayout.addStretch()

        mainLayout.addLayout(buttonsLayout)

    def openImage(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        if imagePath:
            pixmap = QPixmap(imagePath)
            scaled_pixmap = pixmap.scaled(
                self.imageLabel.width(),
                self.imageLabel.height(),
                Qt.AspectRatioMode.KeepAspectRatio,
            )
            self.imageLabel.setPixmap(scaled_pixmap)
            self.controller.setImagePath(imagePath)

    def updateImage(self, img):
        # Convertir l'image en QImage
        img = QPixmap.fromImage(
            QImage(img.data, img.shape[1], img.shape[0], QImage.Format.Format_BGR888)
        )
        # Redimensionner l'image
        scaled_pixmap = img.scaled(
            self.imageLabel.width(),
            self.imageLabel.height(),
            Qt.AspectRatioMode.KeepAspectRatio,
        )
        # Afficher l'image
        self.imageLabel.setPixmap(scaled_pixmap)
