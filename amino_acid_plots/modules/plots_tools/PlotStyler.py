class PlotStyler:
    def __init__(self, subplot, pyplot, position="random"):
        self.subplot = subplot
        self.pyplot = pyplot
        self.position = position
        self.style_plot()

    def style_plot(self):
        self.subplot.set_axisbelow(True)
        self.subplot.set_facecolor('#E6E6E6')
        for spine in self.subplot.spines.values():
            spine.set_visible(False)
        self.subplot.xaxis.tick_bottom()
        self.subplot.yaxis.tick_left()    
        self.subplot.grid(color='w', linestyle='solid')
        self.subplot.tick_params(colors='gray', direction='out')
        for tick in self.subplot.get_xticklabels():
            tick.set_color('gray')
        for tick in self.subplot.get_yticklabels():
            tick.set_color('gray')

        self.subplot.figure.set_figheight(10)

        # if self.position == "random":
        #     self.pyplot.setp(self.subplot.get_xticklabels(), visible=False)
        #     yticks = self.subplot.yaxis.get_major_ticks()
        #     yticks[-1].label1.set_visible(False)

    def set_title(self, text):
        subplot_title = self.subplot.set_title(text, position=(.5, 1.02), backgroundcolor='#C8C8C8', color='white')
        subplot_title_bb = subplot_title.get_bbox_patch()
        subplot_title_bb.set_boxstyle("ext", pad=0.23, width=self.subplot.get_window_extent().width)
        return subplot_title_bb
