from source.pack_loader import load_map_yaml
from source.window_manager import Window

window = Window(1280, 640, "Really? Another Tracker?", 50)

window.create_window()

test = load_map_yaml("./packs/Test-Pack-0.0.1/data/maps/hollow_basin.yaml")
print(test.name)

window.main_loop([], [])
