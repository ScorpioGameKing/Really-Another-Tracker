from source.pack_loader import YAMLLoader
from source.window_manager import Window

window = Window(1280, 640, "Really? Another Tracker?", 50)

window.create_window()

yaml_loader = YAMLLoader()
yaml_loader.load_pack("Test-Pack-0.0.1", window.elements_manager)
#yaml_loader.load_map_yaml("./packs/Test-Pack-0.0.1/data/maps/hollow_basin.yaml")
#yaml_loader.build_map_objects(window.elements_manager)
window.update_maps_panel(yaml_loader.built_maps)

window.main_loop()
