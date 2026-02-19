from pyray import Vector2
from source.map_tools._location_builder import iterate_locations, Location

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
        self.locations = iterate_locations(yaml_data["locations"])
