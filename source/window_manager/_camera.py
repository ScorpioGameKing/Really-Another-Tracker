from pyray import Camera2D, get_mouse_wheel_move, Vector2, get_mouse_position, is_mouse_button_down, is_mouse_button_pressed

class Camera():

    offset: tuple
    target: tuple
    zoom_min: int
    zoom_max: int
    zoom_scale: int
    zoom_scale_min: int
    camera: Camera2D
    mouse_previous: Vector2

    def __init__(self, offset, target, zmin, zmax, zscale, zscalemin, zstart):
        self.offset = offset
        self.target = target
        self.zoom_min = zmin
        self.zoom_max = zmax
        self.zoom_scale = zscale
        self.zoom_scale_min = zscalemin
        self.camera = Camera2D(self.offset, self.target, 0.0, zstart)
        self.mouse_previous = Vector2(0.0, 0.0)
    
    def update(self, in_gui):
        if not in_gui:
            if get_mouse_wheel_move() > 0:
                if self.zoom_scale != 1:
                    self.camera.zoom += self.zoom_scale
                    self.zoom_scale *= 2
                elif self.camera.zoom - self.zoom_scale < self.zoom_max:
                    self.camera.zoom += self.zoom_scale
            elif get_mouse_wheel_move() < 0:
                if self.camera.zoom - self.zoom_scale > self.zoom_min:
                    self.camera.zoom -= self.zoom_scale
                elif self.zoom_scale / 2 > self.zoom_scale_min:
                    self.zoom_scale = self.zoom_scale / 2
                    self.camera.zoom -= self.zoom_scale
        
        if is_mouse_button_pressed(2):
            self.mouse_previous = get_mouse_position()
        if is_mouse_button_down(2):
            self.camera.target = Vector2(
                self.camera.target.x + ((self.mouse_previous.x - get_mouse_position().x) / self.camera.zoom),
                self.camera.target.y + ((self.mouse_previous.y - get_mouse_position().y) / self.camera.zoom))
            self.mouse_previous = get_mouse_position()