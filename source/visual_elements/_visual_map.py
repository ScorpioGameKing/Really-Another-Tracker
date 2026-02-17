from pyray import Texture, load_texture, Vector2, draw_texture_v, WHITE, get_mouse_position, Rectangle

class VisualMap():

    map_data: dict
    map_image: Texture
    map_position: Vector2
    map_location: Rectangle

    def __init__(self, map_data):
        self.map_data = map_data
        self.map_image = load_texture(f"./packs/{self.map_data.image}")
        self.map_position = Vector2(1280 * 50 / 2 , 640 * 50 / 2)
        self.map_location = Rectangle(self.map_position.x, self.map_position.y,
            self.map_position.x + self.map_image.width,
            self.map_position.y + self.map_image.height)
        print(self.map_location.x, self.map_location.y, self.map_location.width, self.map_location.height)
    
    def can_render(self, visible):
        #print(visible)
        if visible:
            return self
        else: return None
    
    def render(self):
        draw_texture_v(self.map_image, self.map_position, WHITE)

        