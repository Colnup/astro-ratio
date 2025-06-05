import cv2
import numpy as np

from .step_abc import ProcessStep
from .process_parameters import IntParameter


class AlphaBetaEnhance(ProcessStep):
    name = "Alpha Beta Enhance"
    parameter_types = {
        "alpha": IntParameter,
        "beta": IntParameter,
    }

    def __init__(self) -> None:
        super().__init__()

        self.alpha: int
        self.beta: int

    def process(self) -> None:
        self._processed_img = cv2.convertScaleAbs(
            self._img.copy(), alpha=self.alpha, beta=self.beta
        )
