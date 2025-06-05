import cv2
import os

from .step_abc import ProcessStep
from .process_parameters import PathParameter


class ImageLoad(ProcessStep):
    name = "Charger une image"
    parameter_types = {
        "path": PathParameter,
    }

    def __init__(self) -> None:
        super().__init__()
        self.path: str = "img/default.png"

    def process(self) -> None:
        self._processed_img = cv2.imread(self.path)
        self._processed_img = cv2.cvtColor(self._processed_img, cv2.COLOR_BGR2RGB)
