from source.map_tools import Location

class VisualLocation():

    location_data: dict[Locations]

    def __init__(self, location_data):
        self.location_data = location_data
        print(self.location_data.name, self.location_data.position.x, self.location_data.position.y)