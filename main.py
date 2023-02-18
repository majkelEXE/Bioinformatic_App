import sys
import sqlite3
from functools import partial
from datetime import date, datetime

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

        mid_layout = QVBoxLayout()
        mid_layout.setContentsMargins(0, 0, 0, 10)  # left, top, right, bottom
        layout.addLayout(mid_layout)

    def sequence_changed(self):
        self.sequence = self.analyseEdit.text()

        # sequence is empty
        if len(self.sequence.strip()) == 0:
            self.analyseButton.setEnabled(False)
            return

        # sequence is invalid
        if check_sequence(self.sequence) == 0:
            self.analyseButton.setEnabled(False)
            return

        self.analyseButton.setEnabled(True)

    def analyse_sequence(self):
        print(check_sequence(self.sequence))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
