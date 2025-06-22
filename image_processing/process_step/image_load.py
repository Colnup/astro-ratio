import cv2

from .process_parameters import PathParameter
from .step_abc import ProcessStep


class ImageLoad(ProcessStep):
    name = "Charger une image"
    PARAMETER_TYPES = {
        "path": PathParameter,
    }

    def __init__(self) -> None:
        super().__init__()
        self.path: str = "img/default.png"

    def process(self) -> None:
        self._processed_img = cv2.imread(self.path)
        self._processed_img = cv2.cvtColor(self._processed_img, cv2.COLOR_BGR2RGB)
