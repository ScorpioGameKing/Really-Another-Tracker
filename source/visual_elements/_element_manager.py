class ElementManager():

    elements: dict

    def __init__(self):
        self.elements = {}

    def add_element(self, element):
        self.elements.update({element.title:element})
    
    def remove_element(self, element):
        self.elements.pop(element.title)
    
    def update(self, gui):
        for i in self.elements:
            self.elements[i].update(gui)

    def render(self):
        for i in self.elements:
            self.elements[i].render()