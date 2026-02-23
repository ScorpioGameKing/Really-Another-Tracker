from yaml import safe_load
from pathlib import Path
from source.map_tools import Map
from source.gui_manager.interfaces import GUIMap

class YAMLLoader():

    loaded_maps: dict
    built_maps: dict
    pack_name: str
    top_level: Path
    map_yamls: []

    def __init__(self):
        self.loaded_maps = {}
        self.built_maps = {}
        self.pack_name = ""
        self.top_level = Path()
        self.map_yamls = []
    
    def load_pack(self, pack_name, elements_manager):
        self.loaded_maps = {}
        self.built_maps = {}
        self.pack_name = pack_name
        self.top_level = Path(f"./packs/{self.pack_name}")
        self.map_yamls = [
            f"{self.top_level}/data/maps/{f.name}" 
            for f in self.top_level.rglob("data/maps/*.yaml") if f.is_file()]
        print(self.map_yamls)
        for my in self.map_yamls:
            self.load_map_yaml(f"./{my}")
        print(self.loaded_maps)
        self.build_map_objects(elements_manager)
        print(self.built_maps)

    def load_map_yaml(self, path:str):
        with open(path) as yaml_map:
            map_data = safe_load(yaml_map)
        
        loaded_map = Map(map_data)
        self.loaded_maps.update({loaded_map.name:loaded_map})
    
    def build_map_objects(self, elements_manager):
        for loaded_map in self.loaded_maps:
            self.built_maps.update({loaded_map:GUIMap(self.loaded_maps[loaded_map], 10,28,35,12, elements_manager)})