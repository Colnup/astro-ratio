from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import (
    QGridLayout,
    QVBoxLayout,
    QLabel,
)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt

from .pipeline import Pipeline
from .process_step import ProcessStep


class RetraitRadient(QWidget):
    MAX_PREVIEW_WIDTH = 600
    MAX_PREVIEW_HEIGHT = 600

    def __init__(self, parent=None):
        super(RetraitRadient, self).__init__(parent)
        self.setWindowTitle("Retrait Radiant")

        # Get the controller from the main application

        ### Définition des layouts ###
        self.main_layout = QGridLayout()
        self.image_layout = QGridLayout()
        self.parameters_layout = QVBoxLayout()

        ###############################################

        ### Définition du layout imageLayout ###
        # self.text_preview = QLabel("Image d'origine")
        # self.text_preview.setAlignment(Qt.AlignmentFlag.AlignBottom)
        # self.text_preview.setMaximumHeight(20)

        # self.image_preview = QLabel()
        # self.image_preview.setMaximumSize(
        #     self.MAX_PREVIEW_WIDTH, self.MAX_PREVIEW_HEIGHT
        # )
        # # self.image_preview.setScaledContents(True)
        # self.image_preview.setPixmap(QPixmap("img/barnard_stacked_gradient.png"))

        self.text_result = QLabel("Traitement actuel :")
        self.text_result.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.text_result.setMaximumHeight(20)
        self.image_result = QLabel()
        self.image_result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_result.setMaximumSize(
            self.MAX_PREVIEW_WIDTH, self.MAX_PREVIEW_HEIGHT
        )

        # self.image_layout.addWidget(self.text_preview, 0, 0)
        # self.image_layout.addWidget(self.image_preview, 1, 0)

        self.image_layout.addWidget(self.text_result, 0, 1)
        self.image_layout.addWidget(self.image_result, 1, 1)

        ### Définition du layout mainLayout ###
        self.pipeline = Pipeline()

        self.main_layout.addWidget(self.pipeline, 0, 0)
        self.main_layout.addLayout(self.image_layout, 0, 1)
        self.main_layout.addLayout(self.parameters_layout, 1, 1)

        # self.mainLayout.addLayout(self.centralLayout)
        self.setLayout(self.main_layout)

        ########## Connexions ##########

        self.pipeline.changeProcessStep.connect(self.update_parameters_widget)
        self.pipeline.changeProcessStep.connect(self.show_result_if_available)
        self.pipeline.processedFinished.connect(self.update_result_image)

    def update_parameters_widget(self, process: ProcessStep):
        # Clear the layout
        for i in reversed(range(self.parameters_layout.count())):
            self.parameters_layout.itemAt(i).widget().setParent(None)

        for parameter in process.get_parameters():
            self.parameters_layout.addWidget(parameter.widget)

    def show_result_if_available(self, process: ProcessStep):
        if process.processed_image is not None:
            self.update_result_image()

    def update_result_image(self):
        image = self.pipeline.current_step.processed_image
        height, width, channel = image.shape
        qimage = QImage(
            image.data, width, height, channel * width, QImage.Format.Format_RGB888
        )

        aspect_ratio = width / height
        scaled_width = min(
            self.MAX_PREVIEW_WIDTH, int(self.MAX_PREVIEW_HEIGHT * aspect_ratio)
        )
        scaled_height = min(
            self.MAX_PREVIEW_HEIGHT, int(self.MAX_PREVIEW_WIDTH / aspect_ratio)
        )
        scaled_qimage = qimage.scaled(scaled_width, scaled_height)

        self.image_result.setPixmap(QPixmap.fromImage(scaled_qimage))
