from pyray import Texture, load_texture, Vector2, draw_texture_v, WHITE, get_mouse_position, Rectangle
from source.visual_elements._visual_location import VisualLocation

class VisualMap():

    map_data: dict
    title: str
    visible: bool
    map_image: Texture
    map_position: Vector2
    map_location: Rectangle
    locations: dict

    def __init__(self, map_data, element_manager):
        self.map_data = map_data
        self.title = map_data.name
        self.visible = False
        self.map_image = load_texture(f"./packs/{self.map_data.image}")
        self.map_position = Vector2(1280 * 50 / 2 , 640 * 50 / 2)
        self.map_location = Rectangle(self.map_position.x, self.map_position.y,
            self.map_image.width,
            self.map_image.height)
        self.locations = {}
        for location in self.map_data.locations:
            self.locations.update({location:VisualLocation(self.map_data.locations[location])})
        element_manager.add_element(self)
  
    def update_postion(self, mouse_previous, mouse_current, camera_zoom):
        self.map_position = Vector2(
            self.map_position.x - ((mouse_previous.x - mouse_current.x) / camera_zoom),
            self.map_position.y - ((mouse_previous.y - mouse_current.y) / camera_zoom))
        self.map_location = Rectangle(self.map_position.x, self.map_position.y,
            self.map_image.width,
            self.map_image.height)
    
    def update(self, gui):
        for location in self.locations:
            self.locations[location].update(self.map_position, gui.interfaces["Location"])

    def render(self):
        if self.visible:
            draw_texture_v(self.map_image, self.map_position, WHITE)
            for location in self.locations:
                self.locations[location].render() 

        