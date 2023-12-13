# controller.py

from image_processing.model import ImageModel
from image_processing.view import MainUI


class Controller:
    def __init__(self):
        self.model = ImageModel()
        self.main_ui = MainUI(self)

    def show(self):
        self.main_ui.show()

    def setImagePath(self, path):
        self.model.image_path = path

    def removeGradient(self):
        img, grad = self.model.remove_gradient()
        # Mettre à jour l'image ici
        self.main_ui.updateImage(img)
