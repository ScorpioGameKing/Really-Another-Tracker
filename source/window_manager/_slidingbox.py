from pyray import Rectangle, gui_panel

class SlidingBox():

    title: str
    min_x: int
    y: int
    w: int
    h: int
    max_x: int
    visible: bool
    location: Rectangle
    panel: gui_panel

    def __init__(self, title, min_x, y, w, h, max_x, visible):
        self.title = title
        self.min_x = min_x
        self.y = y
        self.w = w
        self.h = h
        self.max_x = max_x
        self.visible = visible
        self.location = Rectangle(self.min_x, self.y, self.w, self.h)
        self.panel = gui_panel(self.location, self.title)
    
    def render(self):
        if self.visible and self.location.x != self.max_x:
            self.location.x += 1
        elif not self.visible and self.location.x != self.min_x:
            self.location.x -= 1
        self.panel = gui_panel(self.location, self.title)