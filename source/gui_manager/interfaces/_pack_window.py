from pyray import gui_window_box, Rectangle

class PackWindow():

    position: Rectangle
    title: str

    def __init__(self, position, title):
        self.position = position
        self.title = title

    def update(self):
        pass

    def render(self, state):
        if state:
            gui_window_box(self.position, self.title)