from pyray import draw_rectangle, GREEN, Rectangle, draw_text, BLACK, Color, WHITE
from source.map_tools import Location

class VisualLocation():

    location_data: dict[Locations]
    x: int
    y: int
    width: int
    height: int
    position: Rectangle
    hovering: bool

    def __init__(self, location_data):
        self.location_data = location_data
        self.width = 20
        self.height = 20
        self.x = int(self.location_data.position.x - self.width / 2)
        self.y = int(self.location_data.position.y - self.height / 2)
        self.position = Rectangle(self.x, self.y, self.width, self.height)
        self.hovering = False
        
    def update(self, parent_position):
        self.x = int(self.location_data.position.x + parent_position.x - self.width / 2)
        self.y = int(self.location_data.position.y + parent_position.y - self.height / 2)
        self.position = Rectangle(self.x, self.y, self.width, self.height)
    
    def render(self):
        draw_rectangle(self.x, self.y, self.width, self.height, GREEN)
        if self.hovering:
            draw_rectangle(self.x + 25, self.y, len(self.location_data.name) * 14, 25, Color(124,124,124,186))
            draw_text(self.location_data.name, self.x + 31, self.y + 1, 24, BLACK)
            draw_text(self.location_data.name, self.x + 30, self.y, 24, WHITE)
