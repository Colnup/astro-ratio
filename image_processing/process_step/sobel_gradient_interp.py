"""SobelGradientInterp

Advantages: very precise
Disadvantages: slow, poor performance on images with lots of objects

Method: Compute the edges of the image with laplacian, then blur the computed mask.
        Then, detect the larges area (empty space) in the mask and use that as the
        background. Finally, use the background to interpolate the gradient of the
        image."""


import cv2
import numpy as np

from .step_abc import ProcessStep


class SobelGradientInterp(ProcessStep):
    name = "Sobel Gradient Interpolation"
    parameter_types = {}

    def __init__(self) -> None:
        super().__init__()

    def process(self) -> None:
        gray = cv2.cvtColor(self._img, cv2.COLOR_RGB2GRAY)

        # Compute edges
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        laplacian = cv2.convertScaleAbs(laplacian)

        # Blur edges
        blur = cv2.GaussianBlur(laplacian, (5, 5), 0)

        # Find largest area
        contours, hierarchy = cv2.findContours(
            blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )

        # Find largest contour
        max_area = 0
        max_contour = None
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > max_area:
                max_area = area
                max_contour = contour

        # Create mask
        mask = np.zeros(self._img.shape[:2], np.uint8)
        cv2.drawContours(mask, [max_contour], 0, 255, -1)

        # Get background color
        background = cv2.bitwise_and(self._img, self._img, mask=mask)
        # background = cv2.cvtColor(background, cv2.COLOR_RGB2HSV)
        background = np.mean(background, axis=(0, 1))

        # Interpolate for whole image
        res = self._img.copy()
        for i in range(self._img.shape[0]):
            for j in range(self._img.shape[1]):
                for k in range(3):
                    res[i, j, k] = np.interp(
                        self._img[i, j, k], [background[k], 255], [0, 255]
                    )

        self._processed_img = res
