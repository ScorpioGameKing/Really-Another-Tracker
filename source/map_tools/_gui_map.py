from pyray import gui_label, Rectangle
from source.map_tools._map_builder import Map

class GUIMap():

    map_data: Map
    name: str
    x: int
    y: int
    w: int
    h: int
    location: Rectangle
    label: gui_label

    def __init__(self, map_data, x, y, w, h):
        self.map_data = map_data
        self.name = self.map_data.name
        self.x_in = x
        self.y_in = y
        self.w_in = w
        self.h = h
        self.location = Rectangle(self.x_in, self.y_in, self.w_in, self.h)
        self.label = gui_label(self.location, self.name)
    
    def update(self, parent_location):
        self.location = Rectangle(parent_location.x + self.x_in,
            parent_location.y + self.y_in, 
            parent_location.width - self.w_in,
            self.h)

    def render(self):
        self.label = gui_label(self.location, self.name)

    