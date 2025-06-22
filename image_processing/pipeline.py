import typing

from PyQt6.QtCore import QModelIndex, pyqtSignal
from PyQt6.QtWidgets import (
    QGridLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from .process_step import (
    AVAILABLE_PROCESSES,
    PROCESSES_NAME_TO_CLASSES_HASHMAP,
    ProcessStep,
)


class Pipeline(QWidget):
    """Represents a pipeline in the GUI

    Composed of a list, a button to add a step and a button to remove a step
    """

    change_process_step_signal = pyqtSignal(ProcessStep)
    process_finished_signal = pyqtSignal()

    def __init__(self, parent: typing.Optional["QWidget"] = None) -> None:
        super().__init__(parent)

        ######### Variables ########
        self.auto_process = False
        self.current_step = None

        ######### Layout #########

        self.setMinimumWidth(300)
        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)

        self.available_processes_label = QLabel("Available processes")
        self.available_processes_widget = QListWidget()
        self.available_processes_widget.addItems(
            [step.name for step in AVAILABLE_PROCESSES],
        )

        self.plus_button = QPushButton(">>")
        self.buttons_layout = QVBoxLayout()
        self.buttons_layout.addWidget(self.plus_button)

        self.selected_processes_label = QLabel("Selected processes")
        self.selected_processes_widget = QListWidget()

        self.move_up_button = QPushButton("^")
        self.remove_process_button = QPushButton("Retirer")
        self.move_down_button = QPushButton("v")
        self.buttons_layout.addWidget(self.move_up_button)
        self.buttons_layout.addWidget(self.move_down_button)

        self.mainLayout.addWidget(self.available_processes_label, 0, 0)
        self.mainLayout.addWidget(self.available_processes_widget, 1, 0)
        self.mainLayout.addLayout(self.buttons_layout, 1, 1)
        self.mainLayout.addWidget(self.selected_processes_label, 0, 2)
        self.mainLayout.addWidget(self.selected_processes_widget, 1, 2)
        self.mainLayout.addWidget(self.move_up_button, 2, 2)
        self.mainLayout.addWidget(self.remove_process_button, 3, 2)
        self.mainLayout.addWidget(self.move_down_button, 4, 2)

        ########## Functionnality ##########

        self.selected_processes: list[ProcessStep] = []

        ########## Connects ##########

        # Add
        self.plus_button.clicked.connect(self.plus_button_add_process)
        self.available_processes_widget.doubleClicked.connect(
            self.qlistwidget_add_process,
        )

        # Move buttons
        self.move_up_button.clicked.connect(self.move_up)
        self.move_down_button.clicked.connect(self.move_down)

        # Remove
        self.remove_process_button.clicked.connect(self.remove_process)

        # Select process
        self.selected_processes_widget.currentItemChanged.connect(self.select_process)

    def add_process(self, process: type[ProcessStep]) -> None:
        """Add a process to the pipeline.
        Two entry points: the plus button and the double click on the available list

        Type[ProcessStep] is a type hint to indicate that the argument must be a subclass of ProcessStep,
        and not an instance of ProcessStep.
        """
        # Update the frontend list
        self.selected_processes_widget.addItem(process.name)

        new_process = process()

        for param in new_process.get_parameters():
            param.valueChanged.connect(self.parameter_changed)

        self.selected_processes.append(new_process)
        self.selected_processes_widget.setCurrentRow(
            self.selected_processes_widget.count() - 1,
        )

    def remove_process(self, /) -> None:
        """Remove a process from the pipeline"""
        # Remove from the backend class list
        if self.selected_processes_widget.currentRow() == -1:
            return

        selected_idx = self.selected_processes_widget.currentRow()
        self.selected_processes.pop(selected_idx)
        self.selected_processes_widget.setCurrentRow(selected_idx - 1)
        self.selected_processes_widget.takeItem(selected_idx)

    def plus_button_add_process(self) -> None:
        """Add a process to the pipeline via the button"""

        if self.available_processes_widget.currentItem() is not None:
            process = PROCESSES_NAME_TO_CLASSES_HASHMAP[
                self.available_processes_widget.currentItem().text()
            ]
            return self.add_process(process)

        return None

    def qlistwidget_add_process(self, process: QModelIndex) -> None:
        """Add a process to the pipeline via the available list"""

        self.add_process(PROCESSES_NAME_TO_CLASSES_HASHMAP[process.data()])

    def move_up(self) -> None:
        """Move a process up in the pipeline"""
        if self.selected_processes_widget.currentRow() == -1:
            return

        selected_idx = self.selected_processes_widget.currentRow()
        if selected_idx == 0:
            return

        self.selected_processes_widget.setCurrentRow(selected_idx - 1)

        self.selected_processes_widget.insertItem(
            selected_idx - 1,
            self.selected_processes_widget.takeItem(selected_idx),
        )
        self.selected_processes.insert(
            selected_idx - 1,
            self.selected_processes.pop(selected_idx),
        )

    def move_down(self) -> None:
        """Move a process down in the pipeline"""
        if self.selected_processes_widget.currentRow() == -1:
            return

        selected_idx = self.selected_processes_widget.currentRow()
        if selected_idx == self.selected_processes_widget.count() - 1:
            return

        self.selected_processes_widget.setCurrentRow(selected_idx + 1)

        self.selected_processes_widget.insertItem(
            selected_idx + 1,
            self.selected_processes_widget.takeItem(selected_idx),
        )
        self.selected_processes.insert(
            selected_idx + 1,
            self.selected_processes.pop(selected_idx),
        )

        self.selected_processes_widget.setCurrentRow(selected_idx - 1)

    def select_process(self, _):
        # """Select a process in the pipeline"""
        if self.selected_processes_widget.currentRow() == -1:
            return

        self.current_step = self.selected_processes[
            self.selected_processes_widget.currentRow()
        ]

        self.change_process_step_signal.emit(self.current_step)

    ######## Processing ########

    def process_all(self):
        """Process the image with all the steps in the pipeline"""
        for process, next_process in zip(
            self.selected_processes,
            self.selected_processes[1:],
            strict=False,
        ):
            process.process()
            next_process.load_image(process.processed_image)

        self.selected_processes[-1].process()  # Process the last image
        self.process_finished_signal.emit()

    def set_auto_process(self, auto_process: bool):
        """Set the auto process mode"""
        self.auto_process = auto_process

    def parameter_changed(self, _) -> None:
        """Update the preview if the auto process mode is activated"""
        if self.auto_process:
            self.process_selected_step()

    def process_selected_step(self) -> None:
        """Process the selected step"""

        # Check for previous step results and backtrack if necessary
        selected_idx = self.selected_processes_widget.currentRow()

        current_idx = selected_idx

        while current_idx > 0:
            if self.selected_processes[current_idx - 1].processed_image is None:
                current_idx -= 1
            else:
                break

        # Process the selected step
        for idx in range(current_idx, selected_idx + 1):
            if idx == 0:
                self.selected_processes[idx].process()
            else:
                self.selected_processes[idx].load_image(
                    self.selected_processes[idx - 1].processed_image,
                )
                self.selected_processes[idx].process()

        self.process_finished_signal.emit()
