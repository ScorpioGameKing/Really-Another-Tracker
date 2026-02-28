from pyray import Rectangle, gui_panel, gui_scroll_panel, Vector2

class SlidingBox():

    title: str
    min_x: int
    min_y: int
    max_x: int
    max_y: int
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

    def __init__(self, title, x, y, w, h, scroll_multiplier, visible, slide_direction):
        self.title = title
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.min_x = 0 - self.x - self.w
        self.min_y = 0 - self.y - self.h
        self.max_x = 1280 + self.x + self.w
        self.max_y = 640 + self.y + self.h
        self.visible = visible
        self.slide_direction = slide_direction
        self.location = Rectangle(0,0,0,0)
        self.set_location()
        self.content = Rectangle(0, 0, self.w * 0.9, self.h * scroll_multiplier)
        self.scroll = Vector2(0,0)
        self.view = Rectangle(0,0,0,0)
        self.children = {}
        self.panel = gui_scroll_panel(self.location, self.title, self.content, self.scroll, self.view)
    
    def resize_content(self, width, width_percent, height, height_percent):
        self.content = Rectangle(0, 0, width * width_percent, height * height_percent)
        print(self.content.height)

    def set_location(self):
        match self.slide_direction:
            case "right":
                self.location = Rectangle(self.min_x, self.y, self.w, self.h)
            case "left":
                self.location = Rectangle(self.max_x, self.y, self.w, self.h)
            case "top":
                self.location = Rectangle(self.x, self.min_y, self.w, self.h)
            case "bottom":
                self.location = Rectangle(self.x, self.max_y, self.w, self.h)

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
                if self.visible and self.location.x != self.x:
                    self.location.x -= 1
                elif not self.visible and self.location.x != self.max_x:
                    self.location.x += 1
            case "top":
                if self.visible and self.location.y != self.y:
                    self.location.y += 1
                elif not self.visible and self.location.y != self.max_y:
                    self.location.y -= 1
            case "bottom":
                if self.visible and self.location.y != self.y:
                    self.location.y -= 1
                elif not self.visible and self.location.y != self.max_y:
                    self.location.y += 1

    def render(self):
        self.panel = gui_scroll_panel(self.location, self.title, self.content, self.scroll, self.view)