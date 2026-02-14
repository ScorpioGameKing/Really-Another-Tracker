from pyray import gui_panel, Rectangle, gui_check_box, ffi
from source.map_tools._map_builder import Map

class GUIMap():

    map_data: Map
    name: str
    x: int
    y: int
    w: int
    h: int
    location: Rectangle
    label: gui_panel
    map_enabled: bool
    bool_pass: bool
    enable_check_box: gui_check_box

    def __init__(self, map_data, x, y, w, h):
        self.map_data = map_data
        self.name = self.map_data.name
        self.x_in = x
        self.y_in = y
        self.w_in = w
        self.h = h
        self.location = Rectangle(self.x_in, self.y_in, self.w_in, self.h)
        self.label = gui_panel(self.location, self.name)
        self.map_enabled = ffi.new('bool *', False)
        self.bool_pass = self.map_enabled[0]
        self.enable_check_box = gui_check_box(Rectangle(self.location.x + 5, 
            self.location.y + 25, 20, 20), 
            "Enabled", 
            self.map_enabled)
    
    def update(self, parent_location):
        self.location = Rectangle(parent_location.x + self.x_in,
            parent_location.y + self.y_in, 
            parent_location.width - self.w_in,
            self.h)
        self.bool_pass = self.map_enabled[0]
        self.map_enabled = ffi.new('bool *', self.bool_pass)
        print(self.bool_pass, self.map_enabled[0])
        self.enable_check_box = gui_check_box(Rectangle(self.location.x + 5, 
            self.location.y + 25, 20, 20), 
            "Enabled", 
            self.map_enabled)

    def render(self):
        self.label = gui_panel(self.location, self.name)
        self.enable_check_box = gui_check_box(Rectangle(self.location.x + 5, 
            self.location.y + 25, 20, 20), 
            "Enabled", 
            self.map_enabled)

    