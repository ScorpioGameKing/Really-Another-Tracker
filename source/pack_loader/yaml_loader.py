from yaml import safe_load
from source.map_tools import map_builder

def load_map_yaml(path:str) -> Map:
    with open(path) as yaml_map:
        map_data = safe_load(yaml_map)
    
    loaded_map = map_builder.Map(map_data)
    return loaded_map