class GUIManager():

    interfaces: dict

    def __init__(self):
        self.interfaces = {}

    def add_interface(self, interface):
        self.interfaces.update({interface.title:interface})
    
    def remove_interface(self, interface):
        self.interfaces.pop(interface.title)
    
    def update(self):
        for i in self.interfaces:
            self.interfaces[i].update()

    def render(self):
        for i in self.interfaces:
            self.interfaces[i].render()