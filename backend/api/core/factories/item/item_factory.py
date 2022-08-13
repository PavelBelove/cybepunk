
from core.classes.items.items import Item


class ItemFactory():
    def __init__(self) -> None:
        pass

    def create_item(self, item_data):
        return Item(**item_data)


if __name__ == '__main__':
    from core.character_data.items.inventory_presets import ITEMS_PRESETS

    item_factory = ItemFactory()
    inventory = []

    for i in ITEMS_PRESETS['FIXER']:
        inventory.append(item_factory.create_item(i))
    print(inventory)
