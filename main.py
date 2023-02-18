import sys
from functools import partial

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout, QDateTimeEdit
)

from amino_acid_interpreter.main import check_sequence

from amino_acid_plots.main import PlotsWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setFixedWidth(400)
        self.setWindowTitle("Bioinformatic App")

        self.sequence = ""
        self.analysedSequences = None
        self.frameButtons = []
        self.selectedFrame = None
        self.selectFrameText = None

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

        self.bottom_layout = QVBoxLayout()
        self.bottom_layout.setContentsMargins(0, 0, 0, 10)  # left, top, right, bottom
        layout.addLayout(self.bottom_layout)

        self.emptyText = QLabel("First analyse rna/dna sequence")
        self.emptyText.setAlignment(Qt.AlignCenter)
        self.bottom_layout.addWidget(self.emptyText)

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
        self.clear_bottom_section()
        self.analysedSequences = check_sequence(self.sequence)

        self.selectFrameText = QLabel("Now select frame")
        self.selectFrameText.setAlignment(Qt.AlignCenter)
        self.bottom_layout.addWidget(self.selectFrameText)

        for frameButton in self.frameButtons:
            frameButton.setEnabled(True)

    def change_frame(self, frameNumber):
        self.selectedFrame = frameNumber
        self.generate_frame()

    def clear_bottom_section(self):
        for i in reversed(range(self.bottom_layout.count())):
            widget = self.bottom_layout.itemAt(i).widget()
            if widget is not None:
                self.bottom_layout.itemAt(i).widget().deleteLater()

            layout = self.bottom_layout.itemAt(i).layout()
            if layout is not None:
                while layout.count():
                    layout.takeAt(0).widget().deleteLater()
                layout.deleteLater()

    def generate_frame(self):
        self.clear_bottom_section()

        selectedProteins = self.analysedSequences[f"option{self.selectedFrame}"]
        for i, protein in enumerate(selectedProteins):
            protein_layout = QHBoxLayout()
            protein_layout.setContentsMargins(0, 10, 0, 10)  # left, top, right, bottom
            self.bottom_layout.addLayout(protein_layout)

            proteinIndex = QLabel(f"{str(i + 1)}.")
            proteinIndex.setFixedWidth(15)
            protein_layout.addWidget(proteinIndex)

            proteinName = QLabel(protein)
            protein_layout.addWidget(proteinName)

            visualizationButton = QPushButton("Visualization")
            visualizationButton.setFixedWidth(120)
            visualizationButton.clicked.connect(partial(self.show_visualization, protein))
            protein_layout.addWidget(visualizationButton)

            plotsButton = QPushButton("Plots")
            plotsButton.setFixedWidth(120)
            plotsButton.clicked.connect(partial(self.show_plots, protein))
            protein_layout.addWidget(plotsButton)

    def show_visualization(self, protein):
        print(protein)

    def show_plots(self, protein):
        w.plotsWindow = PlotsWindow(protein)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
