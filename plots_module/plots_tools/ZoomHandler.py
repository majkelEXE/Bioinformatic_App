class ZoomHandler:
    def __init__(self, subplot, pyplot, base_scale, seq_len):
        self.subplot = subplot
        self.pyplot = pyplot
        self.base_scale = base_scale
        self.seq_len = seq_len

        #adjust initial size
        self.adjust_initial_size()
        self.subplot.figure.canvas.mpl_connect('scroll_event',self.zoom_fun)
        


    # def zoom_factory(ax,base_scale = 1.5):
    def zoom_fun(self, event):
        cur_xlim = self.subplot.get_xlim()
        previous_start_x_limit = cur_xlim[0]
        previous_end_x_limit = cur_xlim[1]
        # previous_range = previous_end_x_limit - previous_start_x_limit

        if event.button == 'up':
            scale_factor = 1/self.base_scale
            end_x_limit = previous_end_x_limit*scale_factor
            delta_end = previous_end_x_limit - end_x_limit
            start_x_limit = previous_start_x_limit + delta_end
        elif event.button == 'down':
            scale_factor = self.base_scale
            end_x_limit = previous_end_x_limit*scale_factor
            delta_end = end_x_limit - previous_end_x_limit
            start_x_limit = previous_start_x_limit - delta_end

        else:
            scale_factor = 1

        if end_x_limit - start_x_limit > 5:
            self.subplot.set_xlim([start_x_limit if start_x_limit > 0 else 0,
                     end_x_limit if end_x_limit < self.seq_len else self.seq_len])
        
        self.subplot.figure.canvas.draw_idle()

    def adjust_initial_size(self):
        xlim = self.subplot.get_xlim()
        delta_x_offset = 0 - xlim[0]
        self.subplot.set_xlim(xmin=0, xmax=xlim[1] - delta_x_offset)
        end_x_limit = xlim[1]*1.04
        delta_end = end_x_limit - xlim[1]
        start_x_limit = xlim[0] - delta_end
        if end_x_limit - start_x_limit > 5:
            self.subplot.set_xlim([start_x_limit if start_x_limit > 0 else 0,
                        end_x_limit if end_x_limit < self.seq_len else self.seq_len])
