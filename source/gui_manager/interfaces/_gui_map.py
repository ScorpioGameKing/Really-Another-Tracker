from pyray import gui_panel, Rectangle, gui_check_box, ffi, gui_button
from source.map_tools import Map, Item
from source.visual_elements import VisualMap
from source.gui_manager.interfaces._gui_item import GUIItem

class GUIMap():

    map_data: Map
    visual_map: VisualMap
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
    location_items: dict

    def __init__(self, map_data, x_in, y_in, w_in, h, element_manager):
        self.map_data = map_data
        self.visual_map = VisualMap(self.map_data, element_manager)
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
        self.location_items = {}
        for location in self.map_data.locations:
            items = {}
            item_offset = 0
            for item in self.map_data.locations[location].items:
                items.update({item:GUIItem(
                    self.map_data.locations[location].items[item],
                    5, 45 + (50 * item_offset), 20, 20)})
                item_offset += 1
            self.location_items.update({
                location:items})
    
    def update(self, parent_location, scroll, element_manager):
        self.panel_location = Rectangle(parent_location.x + self.x_in + scroll.x,
            parent_location.y + self.y_in + scroll.y, 
            parent_location.width - self.w_in,
            self.h)
        self.check_location = Rectangle(self.panel_location.x + 5, 
            self.panel_location.y + 25, 20, 20)
        self.center_location = Rectangle(self.panel_location.x + 100, 
            self.panel_location.y + 25, 100, 20)
        element_manager.elements[self.name].visible = self.map_enabled[0]

    def render(self):
        self.label = gui_panel(self.panel_location, self.name)
        self.enable_check_box = gui_check_box(self.check_location, 
            "Enabled", 
            self.map_enabled)
        self.center_on_button = gui_button(self.center_location, 
            "Center On Map")
    