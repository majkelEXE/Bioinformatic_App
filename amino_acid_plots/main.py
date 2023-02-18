import sys

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib.patches import BoxStyle
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication, QLineEdit, QPushButton

from modules.plots_tools.ExtendedTextBox import ExtendedTextBox
from modules.plots_tools.DragHandler import DragHandler
from modules.plots_tools.ResizeHandler import ResizeHandler
from modules.plots_tools.ZoomHandler import ZoomHandler
from modules.plots_tools.PlotStyler import PlotStyler

from modules.analysis_tools.HydropathyCalculator import HydropathyCalculator
from modules.analysis_tools.PolarityCalculator import PolarityCalculator
from modules.analysis_tools.DisordersCalculator import DisordersCalculator

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, sequence="", dpi=80):
        fig = plt.figure(dpi=dpi)
        gs = gridspec.GridSpec(4, 1, height_ratios=[1, 1, 1, 1])
        scale = 1.04
        BoxStyle._style_list["ext"] = ExtendedTextBox

        x_axis = [*range(1, len(sequence) + 1)]

        hydropathy = HydropathyCalculator.hydropathy(*sequence)
        polarity = PolarityCalculator.polarity(*sequence)
        disorder = DisordersCalculator.disorder(sequence)
        disorder_binding = DisordersCalculator.disorder_binding(sequence)

        # first plot
        ax01 = plt.subplot(gs[0])
        ax01.bar(x_axis, hydropathy["values"], width=0.85, color=hydropathy["colors"])
        plot_styler_ax01 = PlotStyler(ax01, plt)
        bb01 = plot_styler_ax01.set_title("Hydropathy")

        # second plot
        ax02 = plt.subplot(gs[1], sharex=ax01)
        ax02.bar(x_axis, polarity["values"], width=0.85, color=polarity["colors"])
        plot_styler_ax02 = PlotStyler(ax02, plt)
        bb02 = plot_styler_ax02.set_title("Polarity")

        ax03 = plt.subplot(gs[2], sharex=ax01)
        ax03.bar(x_axis, disorder["values"], width=0.85, color=disorder["colors"])
        plot_styler_ax03 = PlotStyler(ax03, plt)
        bb03 = plot_styler_ax03.set_title("Disorder")

        ax04 = plt.subplot(gs[3], sharex=ax01)
        ax04.bar(x_axis, disorder_binding["values"], width=0.85, color=disorder_binding["colors"])
        plot_styler_ax04 = PlotStyler(ax04, plt, position="last")
        bb04 = plot_styler_ax04.set_title("Disorder binding")

        self.zoom_handler = ZoomHandler(ax01, plt, base_scale=scale, seq_len=len(x_axis))
        self.drag_handler = DragHandler(ax01, plt)
        self.resize_handler = ResizeHandler(ax01, plt, bb01, bb02, bb03, bb04)

        plt.grid(color='w', linestyle='solid')
        # plt.show()

        plt.tight_layout()

        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.sc = None

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        self.sequence_input = QLineEdit(
            "DDWEIPDGQITVGQRIGSGSFGTVYKGKWHGDVAVKMLNVTAPTPQQLQAFKNEVGVLRKTRHVNILLFMGYSTAPQLAIVTQWCEGSSLYHHLHIIETKFEMIKLIDIARQTAQGMDYLHAKSIIHRDLKSNNIFLHEDLTVKIGDFGLATVKSRWSGSHQFEQLSGSILWMAPEVIRMQDKNPYSFQSDVYAFGIVLYELMTGQLPYSNINNRDQIIFMVGRGYLSPDLSKVRSNCPKAMKRLMAECLKKKRDERPLFPQILASIELLARSLPK")
        self.sequence_input.setPlaceholderText("Enter your DNA or RNA sequence")

        analyse_button = QPushButton("Analyse sequence")
        analyse_button.clicked.connect(self.prepare_analysis)

        self.content_layout = QVBoxLayout()
        self.content_layout.addWidget(self.sequence_input)
        self.content_layout.addWidget(analyse_button)

        # Create a placeholder widget to hold our toolbar and canvas.
        self.widget = QWidget()
        self.widget.setLayout(self.content_layout)
        self.setCentralWidget(self.widget)

        self.show()

    def prepare_analysis(self):
        sequence = self.sequence_input.text()

        if self.sc:
            self.content_layout.removeWidget(self.sc)
            self.sc.setParent(None)

        self.sc = MplCanvas(self, sequence=sequence, dpi=100)
        self.content_layout.addWidget(self.sc)

        self.resize(800, 100 * 10)


app = QApplication(sys.argv)
w = MainWindow()
app.exec_()
