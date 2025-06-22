"""Modules that contain the possible parameters type for the process steps"""

from typing import Any

from PyQt6.QtCore import QObject, Qt, pyqtSignal
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QCheckBox,
    QColorDialog,
    QFileDialog,
    QPushButton,
    QSlider,
    QWidget,
)


class Parameter(QObject):
    """Generic class for a parameter"""

    valueChanged = pyqtSignal(object)

    def __init__(self) -> None:
        super().__init__()
        self._value = None
        self._widget: QWidget = None

    @property
    def value(self) -> Any:
        if self._value is None:
            message = f"No value has been set yet for the parameter {self.__name__}"
            raise Exception(message)
        return self._value

    @property
    def widget(self) -> QWidget:
        return self._widget

    def update_value(self, value: Any) -> None:
        self._value = value
        self.valueChanged.emit(self._value)


class IntParameter(Parameter):
    """Parameter that is an integer"""

    valueChanged = pyqtSignal(int)

    def __init__(self) -> None:
        super().__init__()
        self._min = 0
        self._max = 255
        self._default = self._min

        self._widget = QSlider(Qt.Orientation.Horizontal)
        self._widget.setMinimum(self._min)
        self._widget.setMaximum(self._max)

        self._widget.valueChanged.connect(self.update_value)
        self._widget.setValue(self._default)


class ColorParameter(Parameter):
    """Parameter that is a color"""

    valueChanged = pyqtSignal(tuple)  # tupe[int, int, int]

    def __init__(self) -> None:
        super().__init__()

        self._widget = QPushButton("Choose color")
        self._widget.clicked.connect(self._choose_color)

    def _choose_color(self) -> None:
        color = QColorDialog.getColor()
        if color.isValid():
            self._widget.setStyleSheet(f"background-color: {color.name()}")
            self.update_value(color.getRgb())
        else:
            self._widget.setStyleSheet("background-color: #000000")
            self.update_value(QColor("#000000").getRgb())


class FloatParameter(Parameter):
    """Parameter that is a float"""

    valueChanged = pyqtSignal(float)

    def __init__(self) -> None:
        super().__init__()
        self._min = 0
        self._max = 255
        self._default = self._min

        self._widget = QSlider(Qt.Orientation.Horizontal)
        self._widget.setMinimum(self._min)
        self._widget.setMaximum(self._max)

        self._widget.valueChanged.connect(self.update_value)
        self._widget.setValue(self._default)


class BoolParameter(Parameter):
    """Parameter that is a boolean"""

    valueChanged = pyqtSignal(bool)

    def __init__(self) -> None:
        super().__init__()

        self._widget = QCheckBox()
        self._widget.setChecked(self._default)
        self.widget.stateChanged.connect(self.update_value)


class HSVColorParameter(Parameter):
    """Parameter that is a color, in HSV format"""

    valueChanged = pyqtSignal(tuple)  # tupe[int, int, int]

    def __init__(self) -> None:
        super().__init__()

        self._widget = QPushButton("Choose color")
        self._widget.clicked.connect(self._choose_color)

    def _choose_color(self) -> None:
        color = QColorDialog.getColor()
        if color.isValid():
            self._widget.setStyleSheet(f"background-color: {color.name()}")
            self.update_value(color.getHsv())
        else:
            self._widget.setStyleSheet("background-color: #000000")
            self.update_value(QColor("#000000").getHsv())


class PathParameter(Parameter):
    """Parameter that is a path"""

    valueChanged = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()

        self._widget = QPushButton("Choose file")
        self._widget.clicked.connect(self._choose_file)

    def _choose_file(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(
            self._widget,
            "Open file",
            "",
            "Images Files (*.png *.jpg *.jpeg *.bmp)",
        )
        if file_path:
            self.update_value(file_path)
