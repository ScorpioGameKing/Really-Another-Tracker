def iterate_items(item_data):
    items = dict[Item]
    for item in item_data:
        items.update({item_data[item]["name"]:Item(item_data[item])})
    return items

class Item():

    name: str
    rules: str

    def __init__(self, item_data):
        self.name = item_data["name"]
        self.rules = item_data["rules"]
        #print("Created ITEM:", self.name)