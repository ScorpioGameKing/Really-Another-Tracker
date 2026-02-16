from source.gui_manager.interfaces.base import SlidingBox

class MapPanel(SlidingBox):

    def __init__(self, x, y, w, h, visible):
        super().__init__("Maps", x, y, w, h, visible, "right")
    
    def update(self):
        super().update()
        # Does this need to be a part of base or per basis in the inheriting classes?
        for child in self.children:
            self.children[child].update(self.location)
        
    def render(self):
        super().render()
        for child in self.children:
            self.children[child].render()