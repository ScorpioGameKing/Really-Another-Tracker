from source.gui_manager.interfaces.base import SlidingBox

class MapPanel(SlidingBox):

    def __init__(self, x, y, w, h, visible):
        super().__init__("Maps", x, y, w, h, visible, "right")