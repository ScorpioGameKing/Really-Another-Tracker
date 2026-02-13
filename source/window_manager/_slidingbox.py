from pyray import Rectangle, gui_panel, gui_scroll_panel, Vector2

class SlidingBox():

    title: str
    min_x: int
    x: int
    y: int
    w: int
    h: int
    visible: bool
    location: Rectangle
    panel: gui_panel

    def __init__(self, title, x, y, w, h, visible):
        self.title = title
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.min_x = 0 - self.x - self.w
        self.visible = visible
        self.location = Rectangle(self.min_x, self.y, self.w, self.h)
        self.panel = gui_panel(self.location, self.title)
        #self.panel = gui_scroll_panel(self.location, self.title, Rectangle(0, 0, self.w, self.h*2), Vector2(0,0), Rectangle())

    def render(self):
        if self.visible and self.location.x != self.x:
            self.location.x += 1
        elif not self.visible and self.location.x != self.min_x:
            self.location.x -= 1
        self.panel = gui_panel(self.location, self.title)
        #self.panel = gui_scroll_panel(self.location, self.title, Rectangle(0, 0, self.w, self.h*2), Vector2(0,0), Rectangle())