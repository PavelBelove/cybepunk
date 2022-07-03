from enum import Enum
import uuid
from classes.items.items import Item, Weight


class WeaponType(Enum):
    pass


class Weapon(Item):
    def __init__(self, dict):
        super().__item__(name)
        self.id = uuid.uuid4()
        self.name = dict['name']
        self.mass = dict['mass']
        # self.damage = dict['damage']
        self.hands = dict['hands']
        self.price = dict['price']
        # self.quality = dict['quality']
        self.is_hidden = dict['is_hidden']
        self.dices = dict['dices']
        self.dice_type = dict['dice_type']
