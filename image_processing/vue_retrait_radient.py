from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QComboBox,
    QSlider,
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from image_processing.controller import Controller


class RetraitRadient(QWidget):
    def __init__(self, parent=None):
        super(RetraitRadient, self).__init__(parent)
        self.setWindowTitle("Retrait Radiant")
        self.controller = Controller(self)

        ### Définition des layouts ###

        self.mainLayout = QVBoxLayout()
        self.imageLayout = QHBoxLayout()
        self.imagePreviewLayout = QVBoxLayout()
        self.imageResultLayout = QVBoxLayout()
        self.buttonLayout = QVBoxLayout()

        ###############################################

        ### Définition du layout imageLayout ###
        self.text_preview = QLabel("Image d'origine")
        self.text_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_preview = QLabel()
        self.image_preview.setFixedSize(450, 300)  # Définir la taille du QLabel
        self.image_preview.setScaledContents(True)
        self.image_preview.setPixmap(QPixmap("img/barnard_stacked_gradient.png"))
        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setFixedHeight(300)

        self.text_result = QLabel("Image après retrait du radiant")
        self.text_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_result = QLabel()
        self.image_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_result.setFixedSize(450, 300)
        self.image_result.setScaledContents(True)
        self.image_result.setPixmap(QPixmap("img/barnard_stacked_gradient.png"))

        self.imagePreviewLayout.addWidget(self.text_preview)
        self.imagePreviewLayout.addWidget(self.image_preview)

        self.imageResultLayout.addWidget(self.text_result)
        self.imageResultLayout.addWidget(self.image_result)

        self.imageLayout.addLayout(self.imagePreviewLayout)
        self.imageLayout.addWidget(self.slider)
        self.imageLayout.addLayout(self.imageResultLayout)

        self.mainLayout.addLayout(self.imageLayout)
        self.mainLayout.addLayout(self.buttonLayout)
        self.setLayout(self.mainLayout)

        ###############################################

        ### Définition du layout buttonLayout ###

        self.button_choose_image = QPushButton("Choisir une image")
        self.button_choose_image.clicked.connect(self.controller.choose_image)

        self.button_select_folder = QPushButton("Sélectionner un dossier")
        self.button_select_folder.clicked.connect(self.controller.select_folder)

        self.combo_images = QComboBox()
        self.combo_images.addItem("Sélectionner une image")
        self.combo_images.currentIndexChanged.connect(self.controller.update_images)

        self.combo_gradients = QComboBox()
        self.combo_gradients.addItem("Sélectionner un gradient")
        self.combo_gradients.addItems(self.controller.get_gradients())

        self.button_generate_image = QPushButton("Générer nouvelle image")
        self.button_generate_image.clicked.connect(self.controller.generate_image)

        self.button_download = QPushButton("Télécharger")
        self.button_download.clicked.connect(self.controller.download)

        self.buttonLayout.addWidget(self.button_choose_image)
        self.buttonLayout.addWidget(self.button_select_folder)
        self.buttonLayout.addWidget(self.combo_images)
        self.buttonLayout.addWidget(self.combo_gradients)
        self.buttonLayout.addWidget(self.button_generate_image)
        self.buttonLayout.addWidget(self.button_download)

        ###############################################
