from pyray import Vector2

class Map():
    name: str
    image: str
    rules: list
    locations: dict
    position: Vector2

    def __init__(self, yaml_data):
        self.name = yaml_data["name"]
        self.image = yaml_data["image"]
        self.rules = yaml_data["rules"]
        self.locations = yaml_data["locations"]
