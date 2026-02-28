from pyray import Texture, load_texture, Vector2, draw_texture_v, WHITE, get_mouse_position, Rectangle, draw_rectangle, draw_text, Color, BLACK
from source.visual_elements._visual_location import VisualLocation

class VisualMap():

    map_data: dict
    title: str
    visible: bool
    map_image: Texture
    map_position: Vector2
    map_location: Rectangle
    locations: dict
    hovering: bool

    def __init__(self, map_data, element_manager):
        self.map_data = map_data
        self.title = map_data.name
        self.visible = False
        self.map_image = load_texture(f"./packs/{self.map_data.image}")
        self.map_position = Vector2(1280 * 50 / 2 , 640 * 50 / 2)
        self.map_location = Rectangle(self.map_position.x, self.map_position.y,
            self.map_image.width,
            self.map_image.height)
        self.hovering = False
        self.locations = {}
        for location in self.map_data.locations:
            self.locations.update({location:VisualLocation(self.map_data.locations[location])})
        element_manager.add_element(self)
  
    # Used to update the map's position in worldspace
    def update_postion(self, mouse_previous, mouse_current, camera_zoom):
        self.map_position = Vector2(
            self.map_position.x - ((mouse_previous.x - mouse_current.x) / camera_zoom),
            self.map_position.y - ((mouse_previous.y - mouse_current.y) / camera_zoom))
        self.map_location = Rectangle(self.map_position.x, self.map_position.y,
            self.map_image.width,
            self.map_image.height)
    
    def update(self, gui):

        # Pass the map location for relational positioning and the location panel for location updates
        for location in self.locations:
            self.locations[location].update(self.map_position, gui.interfaces["Location"])

    def render(self):
        if self.visible:
            draw_texture_v(self.map_image, self.map_position, WHITE)
            if self.hovering:
                draw_rectangle(
                    int(self.map_position.x + 25),
                    int(self.map_position.y - 100), 
                    len(self.title) * 28, 54, Color(124,124,124,186))
                draw_text(self.title, 
                    int(self.map_position.x + 31), 
                    int(self.map_position.y - 99), 
                    52, BLACK)
                draw_text(self.title, 
                    int(self.map_position.x + 30), 
                    int(self.map_position.y - 100), 
                    52, WHITE)
            for location in self.locations:
                self.locations[location].render() 

        