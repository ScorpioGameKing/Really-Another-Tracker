from pyray import draw_line, BLACK
from math import floor

def draw_scaling_grid(screen_dimensions:tuple, spacing:int, offset:int, scaling_factor):
    # Scale values
    screen_dimensions = [screen_dimensions[0] * scaling_factor, screen_dimensions[1] * scaling_factor]
    
    # Vertical slices
    for x in range(floor(screen_dimensions[0]/spacing)):
        draw_line((x * spacing) + offset, 0, (x * spacing) + offset, screen_dimensions[1], BLACK)

    # Horizontal slices
    for y in range(floor(screen_dimensions[1]/spacing)):
        draw_line(0, (y * spacing) + offset, screen_dimensions[0], (y * spacing) + offset, BLACK)
