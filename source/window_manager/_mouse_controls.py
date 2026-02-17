from pyray import check_collision_point_rec, get_mouse_position

class MouseController():

    in_gui: bool
    on_element: bool

    def __init__(self):
        self.in_gui = False

    def update(self, gui_interfaces, visual_elements):
        mouse_position = get_mouse_position()
        for interface in gui_interfaces:
            self.in_gui = check_collision_point_rec(
                mouse_position, 
                gui_interfaces[interface].location)
            if self.in_gui:
                break
        for element in visual_elements:
            print(mouse_position.x, mouse_position.y, element.map_location.x, element.map_location.y)
            print(check_collision_point_rec(
                mouse_position, 
                element.map_location))
        
