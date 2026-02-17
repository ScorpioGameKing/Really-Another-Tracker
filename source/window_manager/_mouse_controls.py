from pyray import check_collision_point_rec, get_mouse_position, Vector2

class MouseController():

    in_gui: bool
    on_element: bool

    def __init__(self):
        self.in_gui = False

    def update(self, gui_interfaces, visual_elements, camera):
        mouse_position = get_mouse_position()
        world_position = Vector2(
            mouse_position.x + camera.camera.target.x - camera.camera.offset.x,
            mouse_position.y + camera.camera.target.y - camera.camera.offset.y)
        for interface in gui_interfaces:
            self.in_gui = check_collision_point_rec(
                mouse_position, 
                gui_interfaces[interface].location)
            if self.in_gui:
                break
        for element in visual_elements:
            print(world_position.x, world_position.y, "|", 
                camera.camera.zoom, "|", 
                visual_elements[element].map_location.x, visual_elements[element].map_location.y, 
                visual_elements[element].map_location.width, visual_elements[element].map_location.height)
            print(check_collision_point_rec(
                world_position, 
                visual_elements[element].map_location))
