from pyray import begin_scissor_mode, end_scissor_mode, Rectangle
from source.gui_manager.interfaces.base import SlidingBox

class MapPanel(SlidingBox):

    def __init__(self, x, y, w, h, visible):
        super().__init__("Maps", x, y, w, h, visible, "right")
    
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