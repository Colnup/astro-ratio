# model.py

# Importez les bibliothèques nécessaires, comme cv2 pour le traitement d'image
import cv2
import numpy as np
from scipy.interpolate import RBFInterpolator


class ImageModel:
    def __init__(self):
        self.image_path = ""
        self.gradient_path = "img/gradient_RBF.png"

    def remove_gradient(self):
        """Retire le gradient de l'image."""
        # Charger l'image
        stars = cv2.imread(self.image_path)
        gradient = cv2.imread(self.gradient_path)

        # Redimensionner le gradient pour correspondre à l'image des étoiles
        gradient = cv2.resize(gradient, (stars.shape[1], stars.shape[0]))

        # Convertir les images en float32 pour la soustraction
        stars_float = stars.astype("float32")
        gradient_float = gradient.astype("float32")

        # Soustraire le gradient de l'image des étoiles
        result_float = cv2.subtract(stars_float, gradient_float)

        # Récupere le gradient de l'image et l'enregistre dans un fichier
        # gradient = result_float[0:100, 0:100]

        # Limiter les valeurs à l'intervalle [0, 255] et convertir de nouveau en uint8
        result_image_cv2 = np.clip(result_float, 0, 255).astype("uint8")

        # save

        cv2.imwrite("img/result.png", result_image_cv2)
        # cv2.imwrite("img/result_gradient.png", gradient)

        return result_image_cv2, result_float
