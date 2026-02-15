from pyray import gui_panel, Rectangle, gui_check_box, ffi, gui_button
from source.map_tools._map_builder import Map

class GUIMap():

    map_data: Map
    name: str
    x: int
    y: int
    w: int
    h: int
    panel_location: Rectangle
    check_location: Rectangle
    center_location: Rectangle
    label: gui_panel
    map_enabled: bool
    enable_check_box: gui_check_box
    center_on_button: gui_button

    def __init__(self, map_data, x_in, y_in, w_in, h):
        self.map_data = map_data
        self.name = self.map_data.name
        self.x_in = x_in
        self.y_in = y_in
        self.w_in = w_in
        self.h = h
        self.panel_location = Rectangle(self.x_in, self.y_in, self.w_in, self.h)
        self.check_location = Rectangle(self.panel_location.x + 5, 
            self.panel_location.y + 25, 20, 20)
        self.center_location = Rectangle(self.panel_location.x + 100, 
            self.panel_location.y + 25, 100, 20)
        self.label = gui_panel(self.panel_location, self.name)
        self.map_enabled = ffi.new('bool *', False)
        print(f"Created GUIMap: {self.name}")
    
    def update(self, parent_location):
        self.panel_location = Rectangle(parent_location.x + self.x_in,
            parent_location.y + self.y_in, 
            parent_location.width - self.w_in,
            self.h)
        self.check_location = Rectangle(self.panel_location.x + 5, 
            self.panel_location.y + 25, 20, 20)
        self.center_location = Rectangle(self.panel_location.x + 100, 
            self.panel_location.y + 25, 100, 20)

    def render(self):
        self.label = gui_panel(self.panel_location, self.name)
        self.enable_check_box = gui_check_box(self.check_location, 
            "Enabled", 
            self.map_enabled)
        self.center_on_button = gui_button(self.center_location, 
            "Center On Map")

    