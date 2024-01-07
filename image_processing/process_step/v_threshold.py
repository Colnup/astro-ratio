"""HSV Value Thresholding.

Advantages: Works fast, automatic, good in most cases
Disadvantages: Can remove bright details from the original image
"""

from typing import TypeAlias

import cv2

from step_abc import ProcessStep

HSV: TypeAlias = tuple[int, int, int]


class VThreshold(ProcessStep):
    def __init__(self, value_mask: tuple[HSV, HSV]):
        super().__init__()
        self._value_mask = value_mask

    def process(self) -> None:
        self._processed_img = self._img.copy()
        # Convert to HSV

        mask = cv2.cvtColor(self._processed_img, cv2.COLOR_BGR2HSV)
        # Filter out brightest pixels

        mask = cv2.inRange(mask, self._value_mask[0], self._value_mask[1])
        # Substract mask from image

        mask = cv2.bitwise_not(mask)
        self._processed_img = cv2.bitwise_and(
            self._processed_img, self._processed_img, mask=mask
        )
