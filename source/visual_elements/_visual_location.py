from pyray import draw_rectangle, GREEN, Rectangle
from source.map_tools import Location

class VisualLocation():

    location_data: dict[Locations]
    x: int
    y: int
    width: int
    height: int
    position: Rectangle

    def __init__(self, location_data):
        self.location_data = location_data
        self.width = 20
        self.height = 20
        self.x = int(self.location_data.position.x - self.width / 2)
        self.y = int(self.location_data.position.y - self.height / 2)
        self.position = Rectangle(self.x, self.y, self.width, self.height)
        
    def update(self, parent_position):
        self.x = int(self.location_data.position.x + parent_position.x - self.width / 2)
        self.y = int(self.location_data.position.y + parent_position.y - self.height / 2)
        self.position = Rectangle(self.x, self.y, self.width, self.height)
    
    def render(self):
        draw_rectangle(self.x, self.y, self.width, self.height, GREEN)
    
