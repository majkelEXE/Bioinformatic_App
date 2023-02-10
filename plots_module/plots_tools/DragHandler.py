class DragHandler(object):
    def __init__(self, subplot, pyplot):
        self.subplot = subplot
        self.pressed = False

        self.start_mouse_x_pos = 0

        #these limits are absolute borders, user won't be able to move the chart below the 0 value on the x axis and above the max value
        self.absolute_start_x_limit = self.subplot.get_xlim()[0]
        self.absolute_end_x_limit = self.subplot.get_xlim()[1]

        #these limits can be used when the plot is enlarged, they are used for the actual plot move
        self.start_x_limit = 0
        self.end_x_limit = 0
        
        self.actual_mouse_x_pos = 0
        self.pyplot = pyplot

        self.subplot.figure.canvas.mpl_connect('button_press_event', self.mouse_press)
        self.subplot.figure.canvas.mpl_connect('button_release_event', self.mouse_release)
        self.subplot.figure.canvas.mpl_connect('motion_notify_event', self.mouse_move)

    def mouse_press(self, event):
        self.pressed = True
        self.start_mouse_x_pos = event.xdata
        self.start_x_limit = self.subplot.get_xlim()[0]
        self.end_x_limit = self.subplot.get_xlim()[1]


    def mouse_move(self, event):
        if self.pressed and event.xdata is not None:

            self.actual_mouse_x_pos = event.xdata
            move_delta = self.start_mouse_x_pos - self.actual_mouse_x_pos

            current_start_x_limit = self.start_x_limit + move_delta
            current_end_x_limit = self.end_x_limit + move_delta

            if current_start_x_limit < self.absolute_start_x_limit:
                move_balancer = self.absolute_start_x_limit - current_start_x_limit
                current_start_x_limit = self.absolute_start_x_limit
                current_end_x_limit += move_balancer
            elif current_end_x_limit > self.absolute_end_x_limit:
                move_balancer = self.absolute_end_x_limit - current_end_x_limit
                current_end_x_limit = self.absolute_end_x_limit
                current_start_x_limit += move_balancer

            actual_mouse_from_border_distance = self.subplot.get_xlim()[1] - self.actual_mouse_x_pos

            self.subplot.set_xlim(current_start_x_limit, current_end_x_limit)
            self.subplot.figure.canvas.draw_idle()

            self.start_mouse_x_pos = self.subplot.get_xlim()[1] - actual_mouse_from_border_distance

            self.start_x_limit = self.subplot.get_xlim()[0]
            self.end_x_limit = self.subplot.get_xlim()[1]


    def mouse_release(self, event):
        self.pressed = False