from pyray import begin_scissor_mode, end_scissor_mode, Rectangle, draw_text, BLACK
from source.gui_manager.interfaces.base import SlidingBox

class LocationPanel(SlidingBox):

    name: str
    active_checks: int
    state: str

    def __init__(self, x, y, w, h, visible):
        super().__init__("Location", x, y, w, h, 0.70, visible, "bottom")
        self.location = Rectangle(self.x, self.min_y, self.w, self.h)
        self.name = "REPLACE ME"
        self.active_checks = len(self.children)
        self.state = "PARTIAL"
        self.resize_content(self.w, 0.99, self.h, 0.70)
        #print(x, y, w, h, visible, self.min_y)
    
    def update_display(self, display_items):
        self.children = display_items
        if len(self.children) > 1:
            self.resize_content(self.w, 0.99, self.h, (0.4 * len(self.children)))
        else:
            self.resize_content(self.w, 0.99, self.h, 0.5)
        for item in self.children:
            print(item)
    
    def update(self, element_manager):
        super().update()
        self.active_checks = len(self.children)
        for item in self.children:
            self.children[item].update(self.location, self.scroll)
            if self.children[item].item_found[0]: 
                self.active_checks -= 1
        if self.active_checks == 0:
            print("ALL CHECKS")
        else:
            print("PARTIAL CHECKS", self.active_checks)
        #print("Updating Location Panel")
        
    def render(self):
        super().render()
        begin_scissor_mode(
            int(self.view.x),
            int(self.view.y),
            int(self.view.width), 
            int(self.view.height))
        draw_text(self.name, int(self.view.x + 5), int(self.view.y + 5), 8, BLACK)
        for child in self.children:
            self.children[child].render()
        end_scissor_mode()