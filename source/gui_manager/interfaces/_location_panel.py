from pyray import begin_scissor_mode, end_scissor_mode, Rectangle, draw_text, BLACK
from source.gui_manager.interfaces.base import SlidingBox

class LocationPanel(SlidingBox):

    name: str

    def __init__(self, x, y, w, h, visible):
        super().__init__("Location", x, y, w, h, 1, visible, "bottom")
        self.location = Rectangle(self.x, self.min_y, self.w, self.h)
        self.name = "REPLACE ME"
        #print(x, y, w, h, visible, self.min_y)
    
    def update_display(self, display_items):
        self.children = display_items
        for item in self.children:
            print(item)
    
    def update(self, element_manager):
        super().update()
        for item in self.children:
            self.children[item].update(self.location, self.scroll)
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