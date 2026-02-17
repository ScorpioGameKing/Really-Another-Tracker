from pyray import (
    set_config_flags, 
    init_window, 
    FLAG_WINDOW_RESIZABLE, 
    begin_drawing, 
    clear_background, 
    RAYWHITE, 
    window_should_close, 
    end_drawing,
    close_window,
    begin_mode_2d,
    end_mode_2d, Vector2
)

from source.visual_elements import draw_scaling_grid, ElementManager
from source.window_manager._camera import Camera
from source.window_manager._mouse_controls import MouseController
from source.gui_manager import GUIManager
from source.gui_manager.interfaces import MapPanel

class Window():

    width: int
    height: int
    title: str
    grid_scale: int
    camera: Camera
    mouse_controls: MouseController
    gui: GUIManager
    elements_manager: ElementManager
    render_queue: list

    def __init__(self, width, height, title, grid_scale):
        self.width = width
        self.height = height
        self.title = title
        self.grid_scale = grid_scale

        self.gui = GUIManager()
        self.elements_manager = ElementManager()

        self.camera = Camera(
            Vector2(self.width / 2, self.height / 2),
            Vector2(self.width * self.grid_scale / 2, self.height * self.grid_scale / 2),
            0, 12, 1, 0.125, 3.0)
        
        self.mouse_controls = MouseController()

    def create_window(self):
        # Make the window resizeable BEFORE creation
        set_config_flags(FLAG_WINDOW_RESIZABLE)
        init_window(self.width, self.height, self.title)

        # TODO: Add a more dynamic method of adding and removing interfaces
        # Add the GUI interfaces once and update/render in main
        
        #self.gui.add_interface(SlidingBox("Maps", 20, 72, 240, 540, True, "right"))
        self.gui.add_interface(MapPanel(20, 72, 260, 540, True))

    def update_maps_panel(self, built_maps):
        for built_map in built_maps:
            self.gui.interfaces["Maps"].add_child(built_maps[built_map])

    def main_loop(self):
        while not window_should_close():
            
            # Update everything before the render
            self.gui.update(self.elements_manager)
            self.mouse_controls.update(self.gui.interfaces, self.elements_manager.elements, self.camera)
            self.camera.update(self.mouse_controls.in_gui)

            # Start the render loop with a blank BG
            begin_drawing()
            clear_background(RAYWHITE)
            
            # Draw the 2d features here after the grid
            begin_mode_2d(self.camera.camera)
            draw_scaling_grid([self.width, self.height], 16, 0, self.grid_scale)
            self.elements_manager.render()
            end_mode_2d()
            
            # Draw the GUI last to ensure it's on top
            self.gui.render()
            
            end_drawing()
        close_window()