from pyray import Rectangle, ffi, gui_check_box, gui_button, gui_window_box
from source.gui_manager.interfaces.base import SlidingBox

class ToolbarTabMenu(SlidingBox):

    map_state: bool
    location_state: bool
    pack_window_state: bool

    map_position: Rectangle
    location_position: Rectangle
    pack_position: Rectangle
    pack_window_position: Rectangle

    map_check: gui_check_box
    location_check: gui_check_box
    pack_button: gui_button
    pack_window: gui_window_box

    def __init__(self, x, y, w, h, title, visible):
        super().__init__(title, x, y, w, h, 0.35, visible, "top")
        self.map_state = ffi.new("bool *", True)
        self.location_state = ffi.new("bool *", True)
        self.pack_window_state = False

        self.pack_position = Rectangle(self.x + 5 ,self.y + 25, 80, 20)
        self.map_position = Rectangle(self.x + 90, self.y + 25, 20, 20)
        self.location_position = Rectangle(self.x + 170, self.y + 25, 20, 20)
        self.pack_window_position = Rectangle(320, 120, 320, 320)

        self.pack_button = gui_button(self.pack_position, "Choose Pack")
        self.map_check = gui_check_box(self.map_position, "Map Panel", self.map_state)
        self.location_check_check = gui_check_box(self.location_position, "Location Panel", self.location_state)
        self.pack_window = gui_window_box(self.pack_window_position, "Installed Packs")

    def update(self, element_manager):
        super().update()
        if self.pack_button == True or (self.pack_window == True and self.pack_window_state):
            print("Pressed Pack button or closed window")
            self.pack_window_state = not self.pack_window_state

    def render(self):
        super().render()
        self.pack_button = gui_button(self.pack_position, "Choose Pack")
        self.map_check = gui_check_box(self.map_position, "Map Panel", self.map_state)
        self.location_check_check = gui_check_box(self.location_position, "Location Panel", self.location_state)
        if self.pack_window_state:
            self.pack_window = gui_window_box(self.pack_window_position, "Installed Packs")
        