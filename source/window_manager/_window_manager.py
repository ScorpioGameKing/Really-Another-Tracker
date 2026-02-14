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
    end_mode_2d
)

from source.window_manager._scaling_grid import draw_scaling_grid
from source.window_manager._camera import Camera
from source.window_manager._slidingbox import SlidingBox
from source.window_manager._gui_manager import GUIManager

class Window():

    width: int
    height: int
    title: str
    grid_scale: int
    camera: Camera
    gui: GUIManager

    def __init__(self, width, height, title, grid_scale):
        self.width = width
        self.height = height
        self.title = title
        self.grid_scale = grid_scale

        self.gui = GUIManager()

        self.camera = Camera(
            [self.width / 2, self.height / 2],
            [self.width * self.grid_scale / 2, self.height * self.grid_scale / 2],
            0, 12, 1, 0.125, 3.0)

    def create_window(self):
        # Make the window resizeable BEFORE creation
        set_config_flags(FLAG_WINDOW_RESIZABLE)
        init_window(self.width, self.height, self.title)

        # TODO: Add a more dynamic method of adding and removing interfaces
        # Add the GUI interfaces once and update/render in main
        self.gui.add_interface(SlidingBox("Maps", 20, 72, 240, 540, True))

    def update_maps_panel(self, built_maps):
        for built_map in built_maps:
            print(built_maps[built_map])
            self.gui.interfaces["Maps"].add_child(built_maps[built_map])

    def main_loop(self, *updates:list, **renders:list):
        while not window_should_close():
            
            # Update everything before the render
            self.camera.update()
            self.gui.update()

            # Start the render loop with a blank BG
            begin_drawing()
            clear_background(RAYWHITE)
            
            # Draw the 2d features here after the grid
            begin_mode_2d(self.camera.camera)
            draw_scaling_grid([self.width, self.height], 16, 0, self.grid_scale)
            end_mode_2d()
            
            # Draw the GUI last to ensure it's on top
            self.gui.render()
            
            end_drawing()
        close_window()