from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap
import os


class Controller:
    def __init__(self, view):
        self.view = view
        self.images_path = []
        self.images_name = []

    def choose_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            None,
            "Choisir une image",
            "",
            "Images Files (*.png *.jpg *.jpeg *.bmp)",
        )
        if file_name:
            pixmap = QPixmap(file_name)
            self.view.image_preview.setPixmap(pixmap)

    def get_images(self):
        print(f"Nom des images: {self.images_name}")
        return self.images_name

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(
            None, "Sélectionner un dossier", ""
        )
        if folder_path:
            # print(folder_path)
            image_list = self.load_images_from_folder(folder_path)
            # print(image_list)
            self.images_name = image_list
            self.images_path = [
                os.path.join(folder_path, image) for image in image_list
            ]
            self.update_combo_images()

    def load_images_from_folder(self, folder_path):
        image_list = []
        for filename in os.listdir(folder_path):
            if filename.endswith((".png", ".jpg", ".jpeg", ".bmp")):
                image_list.append(filename)
        return image_list

    def generate_image(self):
        # Logique pour générer une image
        self.view.image_result.setPixmap(QPixmap("img/sucette.png"))

    def download(self):
        # Logique pour télécharger une image
        pass

    def get_gradients(self):
        # Logique pour récupérer tous les gradients dans un dossier
        return ["Magie noire", "Gradient 2", "Gradient 3"]

    def update_combo_images(self):
        self.view.combo_images.clear()
        self.view.combo_images.addItem("Sélectionner une image")
        self.view.combo_images.addItems(self.get_images())

    def update_images(self):
        if self.view.combo_images.currentText() != "Sélectionner une image":
            image_name = self.view.combo_images.currentText()
            image_path = next(
                (path for path in self.images_path if image_name in path), None
            )
            if image_path is not None:
                self.view.image_preview.setPixmap(QPixmap(image_path))
