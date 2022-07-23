import uuid

from classes.items.items import Item, Weight


class Implant(Item):
    def __init__(self, dict):
        super().__init__(dict['name'], mass=Weight.implant)
        self.id = uuid.uuid4()
        # self.damage = dict['damage']
        self.slot = dict['slot']
        self.price = dict['price']
        # self.quality = dict['quality']
        self.is_hidden = dict['is_hidden']
        self.dices = dict['dices']
        self.dice_type = dict['dice_type']
