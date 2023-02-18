import sys
from functools import partial

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout, QDateTimeEdit
)

from amino_acid_interpreter.main import check_sequence


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(400)
        self.setWindowTitle("Bioinformatic App")

        self.sequence = ""
        self.analysedSequences = None
        self.frameButtons = []
        self.selectedFrame = None

        container = QWidget()
        self.setCentralWidget(container)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        container.setLayout(layout)

        top_layout = QHBoxLayout()
        top_layout.setAlignment(Qt.AlignCenter)
        top_layout.setContentsMargins(0, 10, 0, 10)  # left, top, right, bottom
        layout.addLayout(top_layout)

        self.analyseEdit = QLineEdit()
        self.analyseEdit.setPlaceholderText("Enter DNA or RNA sequence")
        self.analyseEdit.textChanged.connect(self.sequence_changed)
        top_layout.addWidget(self.analyseEdit)

        self.analyseButton = QPushButton("Analyse")
        self.analyseButton.setFixedWidth(120)
        self.analyseButton.setEnabled(False)
        self.analyseButton.clicked.connect(self.analyse_sequence)
        top_layout.addWidget(self.analyseButton)

        mid_layout = QHBoxLayout()
        mid_layout.setContentsMargins(0, 0, 0, 10)  # left, top, right, bottom
        layout.addLayout(mid_layout)

        for i in range(1, 4):
            frameButton = QPushButton(f"Frame {i}")
            frameButton.setFixedWidth(120)
            frameButton.setEnabled(False)
            frameButton.clicked.connect(partial(self.change_frame, i))
            mid_layout.addWidget(frameButton)
            self.frameButtons.append(frameButton)

    def sequence_changed(self):
        self.sequence = self.analyseEdit.text()
        self.analyseEdit.setText(self.sequence.upper())
        self.validate_sequence()

    def validate_sequence(self):
        valid = True

        # sequence is empty
        if len(self.sequence.strip()) == 0:
            valid = False

        # sequence is invalid
        if check_sequence(self.sequence) == 0:
            valid = False

        self.analyseButton.setEnabled(valid)

    def analyse_sequence(self):
        self.analysedSequences = check_sequence(self.sequence)

        for frameButton in self.frameButtons:
            frameButton.setEnabled(True)

    def change_frame(self, frameNumber):
        self.selectedFrame = frameNumber
        print(self.selectedFrame)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
