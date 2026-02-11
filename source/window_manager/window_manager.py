from pyray import (
    set_config_flags, 
    init_window, 
    FLAG_WINDOW_RESIZABLE, 
    begin_drawing, 
    clear_background, 
    RAYWHITE, 
    window_should_close, 
    end_drawing,
    close_window
)

def create_window():
    set_config_flags(FLAG_WINDOW_RESIZABLE)
    init_window(1280, 640, "Really? Another Tracker?")

def main_loop():
    while not window_should_close():
        begin_drawing()
        clear_background(RAYWHITE)
        end_drawing()
    close_window()