from matplotlib.path import Path

class ExtendedTextBox:
    def __init__(self, pad=0.3, width=500.):
        self.width = width
        self.pad = pad
        super().__init__()

    def __call__(self, x0, y0, width, height, mutation_size):
        pad = mutation_size * self.pad
        height = height + 2.*pad
        y0 = y0 - pad
        y1 = y0 + height
        _x0 = x0
        x0 = _x0 +width /2. - self.width/2.
        x1 = _x0 +width /2. + self.width/2.
        return Path([(x0, y0),
                     (x1, y0), (x1, y1), (x0, y1),
                     (x0, y0)],
                    closed=True)