from pyray import Vector2
from source.map_tools._item_builder import Item, iterate_items

def iterate_locations(location_data):
    locations = dict[Location]
    for location in location_data:
        locations.update({location_data[location]["name"]:Location(location_data[location])})
    return locations

class Location():

    name: str
    rules: str
    items: dict[Item]
    postion: Vector2

    def __init__(self, location_data):
        self.name = location_data["name"]
        self.rules = location_data["rules"]
        self.items = iterate_items(location_data["items"])
        #print("LOCATION:", self.name)