class ResizeHandler:
    def __init__(self, subplot, pyplot, *subplots_bb):
        self.subplot = subplot
        self.pyplot = pyplot
        self.subplots_bb = subplots_bb
        # self.subplot.figure.canvas.mpl_connect('button_press_event', self.on_resize)
        self.pyplot.gcf().canvas.mpl_connect('resize_event', self.on_resize)

    def on_resize(self, event):
        self.pyplot.tight_layout()
        for subplot_bb in self.subplots_bb:
            subplot_bb.set_boxstyle("ext", pad=0.4, width=self.subplot.get_window_extent().width )
