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

class Window():

    width: int
    height: int
    title: str
    grid_scale: int
    camera: Camera

    def __init__(self, width, height, title, grid_scale):
        self.width = width
        self.height = height
        self.title = title
        self.grid_scale = grid_scale

        self.camera = Camera(
            [self.width / 2, self.height / 2],
            [self.width * self.grid_scale / 2, self.height * self.grid_scale / 2],
            0, 12, 1, 0.125, 3.0)

    def create_window(self):
        set_config_flags(FLAG_WINDOW_RESIZABLE)
        init_window(self.width, self.height, self.title)

    def main_loop(self, *updates:list, **renders:list):
        while not window_should_close():
            begin_drawing()
            clear_background(RAYWHITE)
            begin_mode_2d(self.camera.camera)

            draw_scaling_grid([self.width, self.height], 16, 0, self.grid_scale)
            self.camera.update()

            for update in updates:
                pass            

            for render in renders:
                pass
            
            end_mode_2d()
            end_drawing()
        close_window()