from pyray import Rectangle, gui_panel, gui_scroll_panel, Vector2

class SlidingBox():

    title: str
    min_x: int
    x: int
    y: int
    w: int
    h: int
    visible: bool
    slide_direction: str
    location: Rectangle
    content_view: Rectangle
    scroll: Vector2
    panel: gui_panel
    children: dict

    def __init__(self, title, x, y, w, h, visible, slide_direction):
        self.title = title
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.min_x = 0 - self.x - self.w
        self.visible = visible
        self.slide_direction = slide_direction
        self.location = Rectangle(self.min_x, self.y, self.w, self.h)
        self.content = Rectangle(0, 0, self.w, self.h*2)
        self.scroll = Vector2(0,0)
        self.view = Rectangle()
        self.children = {}
        #self.panel = gui_panel(self.location, self.title)
        self.panel = gui_scroll_panel(self.location, self.title, self.content, self.scroll, self.view)

    def add_child(self, child):
        self.children.update({child.name:child})

    def update(self):
        match self.slide_direction:
            case "right":
                if self.visible and self.location.x != self.x:
                    self.location.x += 1
                elif not self.visible and self.location.x != self.min_x:
                    self.location.x -= 1
            case "left":
                print("Slide from left")
            case "top":
                print("Slide from top")
            case "Bottom":
                print("Slide from bottom")

    def render(self):
        #self.panel = gui_panel(self.location, self.title)
        self.panel = gui_scroll_panel(self.location, self.title, self.content, self.scroll, self.view)