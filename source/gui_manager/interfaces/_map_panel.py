from pyray import begin_scissor_mode, end_scissor_mode, Rectangle
from source.gui_manager.interfaces.base import SlidingBox

class MapPanel(SlidingBox):

    def __init__(self, x, y, w, h, visible):
        super().__init__("Maps", x, y, w, h, 0.7, visible, "right")
        self.location = Rectangle(self.min_x, self.y, self.w, self.h)
    
    def update_display(self):
        panel_offset = 0
        if len(self.children) > 1:
            for mp in self.children:
                panel_y_location = 50 * panel_offset
                self.children[mp].update_panel(panel_y_location)
                panel_offset += 1
            self.resize_content(self.w, 0.99, self.h, (0.4 * len(self.children)))
        else:
            self.resize_content(self.w, 0.99, self.h, 0.5)
    
    def update(self, element_manager):
        super().update()
        # Does this need to be a part of base or per basis in the inheriting classes?
        for child in self.children:
            self.children[child].update(self.location, self.scroll, element_manager)
        
    def render(self):
        super().render()
        begin_scissor_mode(int(self.view.x),
            int(self.view.y),
            int(self.view.width), 
            int(self.view.height))
        for child in self.children:
            self.children[child].render()
        end_scissor_mode()