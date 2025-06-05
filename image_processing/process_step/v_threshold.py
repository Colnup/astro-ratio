"""HSV Value Thresholding.

Advantages: Works fast, automatic, good in most cases
Disadvantages: Can remove bright details from the original image
"""


import cv2
from PyQt6.QtGui import QColor  # Typing only

from .step_abc import ProcessStep
from .process_parameters import IntParameter


class VThreshold(ProcessStep):
    name = "Value Thresholding"
    parameter_types = {
        "max_value": IntParameter,
    }

    def __init__(self) -> None:
        super().__init__()

        self.max_value: int = 0

    def process(self) -> None:
        self._processed_img = self._img.copy()

        # Convert to HSV
        mask = cv2.cvtColor(self._processed_img, cv2.COLOR_BGR2HSV)

        # Filter out brightest pixels
        mask = cv2.inRange(mask, (0, 0, 0), (255, 255, self.max_value))

        # Substract mask from image
        mask = cv2.bitwise_not(mask)
        self._processed_img = cv2.bitwise_and(
            self._processed_img, self._processed_img, mask=mask
        )
