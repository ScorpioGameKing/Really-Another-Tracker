from pyray import gui_window_box, Rectangle

class PackWindow():

    position: Rectangle
    title: str
    window: gui_window_box

    def __init__(self, position, title):
        self.position = position
        self.title = title
        self.window = gui_window_box(self.position, self.title)

    def update(self):
        pass

    def render(self, state):
        if state:
            self.window = gui_window_box(self.position, self.title)