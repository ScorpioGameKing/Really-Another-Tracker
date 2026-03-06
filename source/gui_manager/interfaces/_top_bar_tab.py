from pyray import Rectangle, ffi, gui_check_box, gui_button, gui_window_box
from source.gui_manager.interfaces.base import SlidingBox
from source.gui_manager.interfaces._pack_window import PackWindow

class ToolbarTabMenu(SlidingBox):

    map_state: bool
    location_state: bool
    pack_window_state: bool
    item_state: bool
    load_state: bool
    save_state: bool

    map_position: Rectangle
    location_position: Rectangle
    pack_position: Rectangle
    pack_window_position: Rectangle
    item_position: Rectangle
    save_position: Rectangle
    load_position: Rectangle

    map_check: gui_check_box
    location_check: gui_check_box
    pack_button: gui_button
    pack_window: gui_window_box
    item_check: gui_check_box
    save_button: gui_button
    load_button: gui_button

    def __init__(self, x, y, w, h, title, visible):
        super().__init__(title, x, y, w, h, 0.35, visible, "top")
        self.map_state = ffi.new("bool *", True)
        self.location_state = ffi.new("bool *", True)
        self.item_state = ffi.new("bool *", True)
        self.pack_window_state = False
        self.save_state = False
        self.load_state = False

        self.pack_position = Rectangle(
            self.x + 5, 
            self.y + 25, 
            80, 20)
        self.save_position = Rectangle(
            self.pack_position.x + self.pack_position.width + 5, 
            self.y + 25, 
            50, 20)
        self.load_position = Rectangle(
            self.save_position.x + self.save_position.width + 5, 
            self.y + 25, 
            50, 20)
        self.map_position = Rectangle(
            self.load_position.x + self.load_position.width + 5, 
            self.y + 25, 
            20, 20)
        self.location_position = Rectangle(
            self.map_position.x + self.map_position.width + 5 + 55, 
            self.y + 25, 
            20, 20)
        self.item_position = Rectangle(
            self.location_position.x + self.location_position.width + 5 + 80, 
            self.y + 25, 
            20, 20)
        self.pack_window_position = Rectangle(290, 72, 700, 370)

        self.pack_button = gui_button(self.pack_position, "Choose Pack")
        self.save_button = gui_button(self.save_position, "Save")
        self.load_button = gui_button(self.load_position, "Load")
        self.map_check = gui_check_box(self.map_position, "Map Panel", self.map_state)
        self.location_check = gui_check_box(self.location_position, "Location Panel", self.location_state)
        self.item_check = gui_check_box(self.item_position, "Item Panel", self.item_state)
        self.pack_window = PackWindow(self.pack_window_position, "Installed Packs")

    def update(self, element_manager):
        super().update()
        if self.pack_button == True or (self.pack_window.window == True and self.pack_window_state):
            self.pack_window_state = not self.pack_window_state

    def render(self):
        super().render()
        self.pack_button = gui_button(self.pack_position, "Choose Pack")
        self.save_button = gui_button(self.save_position, "Save")
        self.load_button = gui_button(self.load_position, "Load")
        self.map_check = gui_check_box(self.map_position, "Map Panel", self.map_state)
        self.location_check = gui_check_box(self.location_position, "Location Panel", self.location_state)
        self.item_check = gui_check_box(self.item_position, "Item Panel", self.item_state)
        self.pack_window.render(self.pack_window_state)
        