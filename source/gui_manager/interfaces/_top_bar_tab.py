from pyray import Rectangle, ffi, gui_check_box
from source.gui_manager.interfaces.base import SlidingBox

class ToolbarTabMenu(SlidingBox):

    map_state: bool
    location_state: bool
    map_position: Rectangle
    location_position: Rectangle
    map_check: gui_check_box
    location_check: gui_check_box
    
    def __init__(self, x, y, w, h, title, visible):
        super().__init__(title, x, y, w, h, 0.35, visible, "top")
        self.map_state = ffi.new("bool *", True)
        self.location_state = ffi.new("bool *", True)
        self.map_position = Rectangle(self.x + 5, self.y + 25, 20, 20)
        self.location_position = Rectangle(self.x + 90, self.y + 25, 20, 20)

    def update(self, element_manager):
        super().update()

    def render(self):
        super().render()
        self.map_check = gui_check_box(self.map_position, "Map Panel", self.map_state)
        self.location_check_check = gui_check_box(self.location_position, "Location Panel", self.location_state)
        