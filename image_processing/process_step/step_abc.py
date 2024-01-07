from abc import ABC, abstractmethod

from numpy.typing import NDArray
import cv2


class ProcessStep(ABC):
    def __init__(self) -> None:
        self._img = None
        self._processed_img = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"

    # Concrete methods

    def write_to_file(self, path: str) -> None:
        cv2.imwrite(path, self._processed_img)

    # Abstract methods

    @abstractmethod
    def process(self) -> None:
        # Process the image in some way
        pass

    # Abstract class methods

    @abstractmethod
    @classmethod
    def from_image_path(cls, path: str) -> "ProcessStep":
        # Load the image from the path
        pass

    @abstractmethod
    @classmethod
    def from_image(cls, img: NDArray) -> "ProcessStep":
        # Load the image from the array
        pass

    # Properties

    @property
    def original_image(self) -> NDArray:
        return self._img

    @property
    def processed_image(self) -> NDArray:
        return self._processed_img
