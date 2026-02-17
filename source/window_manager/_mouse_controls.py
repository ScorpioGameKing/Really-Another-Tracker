from pyray import check_collision_point_rec, get_mouse_position, is_mouse_button_down, is_mouse_button_pressed, Vector2, Rectangle, draw_line, RED

class MouseController():

    in_gui: bool
    on_element: bool
    mouse_previous: Vector2

    def __init__(self):
        self.in_gui = False
        self.mouse_previous = Vector2(0.0, 0.0)

    def update(self, gui_interfaces, visual_elements, camera):
        mouse_position = get_mouse_position()
        world_position = Vector2(
            (mouse_position.x / camera.camera.zoom)+ camera.camera_corner.x,
            (mouse_position.y / camera.camera.zoom) + camera.camera_corner.y)
        
        for interface in gui_interfaces:
            self.in_gui = check_collision_point_rec(
                mouse_position, 
                gui_interfaces[interface].location)
            if self.in_gui:
                break
        for element in visual_elements:
            hovering = check_collision_point_rec(
                world_position, 
                visual_elements[element].map_location)
            if hovering:
                if is_mouse_button_pressed(0):
                    self.mouse_previous = get_mouse_position()
                if is_mouse_button_down(0):
                    visual_elements[element].map_position = Vector2(
                        visual_elements[element].map_position.x - ((self.mouse_previous.x - get_mouse_position().x) / camera.camera.zoom),
                        visual_elements[element].map_position.y - ((self.mouse_previous.y - get_mouse_position().y) / camera.camera.zoom))
                    visual_elements[element].map_location = Rectangle(visual_elements[element].map_position.x, visual_elements[element].map_position.y,
                    visual_elements[element].map_image.width,
                    visual_elements[element].map_image.height)
                    self.mouse_previous = get_mouse_position()
    
    # For debug reasons, can remove later
    def render(self, camera):
        mouse_position = get_mouse_position()
        world_position = Vector2(
            (mouse_position.x / camera.camera.zoom)+ camera.camera_corner.x,
            (mouse_position.y / camera.camera.zoom) + camera.camera_corner.y)
        draw_line(int(camera.camera_corner.x), int(camera.camera_corner.y), int(world_position.x), int(world_position.y), RED)
