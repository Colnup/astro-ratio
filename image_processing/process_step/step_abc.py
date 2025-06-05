from abc import ABC, abstractmethod
from typing import Callable, Type

from numpy.typing import NDArray
import cv2
from PyQt6.QtCore import pyqtSignal, QObject

from .process_parameters import Parameter


class ProcessStep(ABC):
    name: str
    parameter_types: dict[str, Type[Parameter]]

    def __init__(self) -> None:
        self._img = None
        self._processed_img = None

        for key, val in self.parameter_types.items():
            setattr(self, key, None)

            parameter = val()
            setattr(self, f"{key}_instance", parameter)
            parameter.valueChanged.connect(self.update_parameter(key))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    # Concrete methods

    def write_to_file(self, path: str) -> None:
        cv2.imwrite(path, self._processed_img)

    def load_image(self, img: NDArray) -> None:
        """Basic image loading. Might get overriden in subclasses to
        have more specific loading."""
        self._img = img

    def update_parameter(self, key: str) -> Callable[..., None]:
        def update(value):
            setattr(self, key, value)

        return update

    def get_parameters(self) -> list[Parameter]:
        return [getattr(self, f"{key}_instance") for key in self.parameter_types.keys()]

    # Abstract methods

    @abstractmethod
    def process(self) -> None:
        # Process the image in some way
        pass

    # Properties

    @property
    def original_image(self) -> NDArray:
        return self._img

    @property
    def processed_image(self) -> NDArray:
        # if self._processed_img is None:
        #     self.process()

        return self._processed_img
