import cv2

from .process_parameters import IntParameter
from .step_abc import ProcessStep


class AlphaBetaEnhance(ProcessStep):
    name = "Alpha Beta Enhance"
    PARAMETER_TYPES = {
        "alpha": IntParameter,
        "beta": IntParameter,
    }

    def __init__(self) -> None:
        super().__init__()

        self.alpha: int
        self.beta: int

    def process(self) -> None:
        self._processed_img = cv2.convertScaleAbs(
            self._img.copy(),
            alpha=self.alpha,
            beta=self.beta,
        )
