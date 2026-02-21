from pyray import check_collision_point_rec, get_mouse_position, is_mouse_button_down, is_mouse_button_pressed, Vector2, Rectangle, draw_line, RED

class MouseController():

    in_gui: bool
    on_element: bool
    mouse_previous: Vector2

    def __init__(self):
        self.in_gui = False
        self.mouse_previous = Vector2(0.0, 0.0)

    def update(self, gui_interfaces, visual_elements, camera):

        # Determin the mouse position in the window and the world position relative to the camera
        mouse_position = get_mouse_position()
        world_position = Vector2(
            (mouse_position.x / camera.camera.zoom)+ camera.camera_corner.x,
            (mouse_position.y / camera.camera.zoom) + camera.camera_corner.y)
        
        # Iterate through the GUI Interfaces to disable zoom when over one
        for interface in gui_interfaces:
            self.in_gui = check_collision_point_rec(
                mouse_position, 
                gui_interfaces[interface].location)
            if self.in_gui:
                break
        
        # Iterate through the 2D Elements to do a lot
        for element in visual_elements:

            # See if we're on a map to enable drag and drop
            hovering_map = check_collision_point_rec(
                world_position, 
                visual_elements[element].map_location)

            # If we're on a map and it's visible we can move it
            if hovering_map and visual_elements[element].visible:
                
                # Iterate locations first to see if there's any UI Updates to pass on
                for location in visual_elements[element].locations:
                    
                    # Before drag and drop, check if we're over a location to update the location menu
                    hovering_location = check_collision_point_rec(
                        world_position, 
                        visual_elements[element].locations[location].position)
                    if hovering_location:
                        visual_elements[element].locations[location].hovering = True
                        if is_mouse_button_pressed(0):
                            gui_interfaces["Location"].name = location
                            gui_interfaces["Location"].update_display(
                                gui_interfaces["Maps"].children[visual_elements[element].title].location_items[location])
                    else:
                        visual_elements[element].locations[location].hovering = False
                
                # When we first press the mouse, save the current position
                if is_mouse_button_pressed(0):
                    self.mouse_previous = get_mouse_position()
                
                # While we're holding the mouse button down, pass the current, previous and camera zoom to
                # move the element's position scaled properly
                if is_mouse_button_down(0):
                    visual_elements[element].update_postion(self.mouse_previous, get_mouse_position(), camera.camera.zoom)
                    self.mouse_previous = get_mouse_position()
    
    # For debug reasons, can remove later
    def render(self, camera):
        mouse_position = get_mouse_position()
        world_position = Vector2(
            (mouse_position.x / camera.camera.zoom)+ camera.camera_corner.x,
            (mouse_position.y / camera.camera.zoom) + camera.camera_corner.y)
        draw_line(int(camera.camera_corner.x), int(camera.camera_corner.y), int(world_position.x), int(world_position.y), RED)
