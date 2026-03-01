class GUIManager():

    interfaces: dict

    def __init__(self):
        self.interfaces = {}

    def add_interface(self, interface):
        self.interfaces.update({interface.title:interface})
    
    def remove_interface(self, interface):
        self.interfaces.pop(interface.title)
    
    def update(self, element_manager):
        for i in self.interfaces:
            match i:
                case "Maps":
                    self.interfaces[i].visible = self.interfaces["Settings"].map_state[0]
                case "Location":
                    self.interfaces[i].visible = self.interfaces["Settings"].location_state[0]
            self.interfaces[i].update(element_manager)

    def render(self):
        for i in self.interfaces:
            self.interfaces[i].render()