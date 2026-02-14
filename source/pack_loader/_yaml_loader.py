from yaml import safe_load
from source.map_tools import Map, GUIMap

class YAMLLoader():

    loaded_maps: dict
    built_maps: dict

    def __init__(self):
        self.loaded_maps = {}
        self.built_maps = {}

    def load_map_yaml(self, path:str):
        with open(path) as yaml_map:
            map_data = safe_load(yaml_map)
        
        loaded_map = Map(map_data)
        self.loaded_maps.update({loaded_map.name:loaded_map})
    
    def build_map_objects(self):
        for loaded_map in self.loaded_maps:
            self.built_maps.update({loaded_map:GUIMap(self.loaded_maps[loaded_map], 10,25,20,10)})