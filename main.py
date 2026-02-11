from source.pack_loader import yaml_loader
from source.window_manager import window_manager

window_manager.create_window()

test = yaml_loader.load_map_yaml("./packs/Test-Pack-0.0.1/data/maps/hollow_basin.yaml")
print(test.name)

window_manager.main_loop()
