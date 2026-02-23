from pyray import draw_rectangle, GREEN, ORANGE, RED, GRAY, Rectangle, draw_text, BLACK, Color, WHITE
from source.map_tools import Location

class VisualLocation():

    location_data: dict
    x: int
    y: int
    width: int
    height: int
    position: Rectangle
    hovering: bool
    state: str
    state_color: Color

    def __init__(self, location_data):
        self.location_data = location_data
        self.width = 20
        self.height = 20
        self.x = int(self.location_data.position.x - self.width / 2)
        self.y = int(self.location_data.position.y - self.height / 2)
        self.position = Rectangle(self.x, self.y, self.width, self.height)
        self.hovering = False
        self.state_color = GREEN
    
    def update_state(self, location_panel):
        if self.location_data.name == location_panel.name:
            self.state = location_panel.state
            match self.state:
                case "FULL":
                    self.state_color = GREEN
                    #print("Set to GREEN")
                case "PARTIAL":
                    self.state_color = ORANGE
                    #print("Set to ORANGE")
                case "COMPLETE":
                    self.state_color = GRAY
                    #print("Set to GRAY")
                case _:
                    self.state_color = RED
                    #print("Set to RED")
        
    def update(self, parent_position, gui):
        self.update_state(gui)
        self.x = int(self.location_data.position.x + parent_position.x - self.width / 2)
        self.y = int(self.location_data.position.y + parent_position.y - self.height / 2)
        self.position = Rectangle(self.x, self.y, self.width, self.height)
    
    def render(self):
        draw_rectangle(self.x, self.y, self.width, self.height, self.state_color)
        if self.hovering:
            draw_rectangle(self.x + 25, self.y, len(self.location_data.name) * 14, 25, Color(124,124,124,186))
            draw_text(self.location_data.name, self.x + 31, self.y + 1, 24, BLACK)
            draw_text(self.location_data.name, self.x + 30, self.y, 24, WHITE)
