from enum import Enum
import uuid
from core.classes.items.items import Item, Weight


class WeaponType(Enum):
    pass


class Weapon(Item):
    def __init__(self, dict):
        super().__init__(dict['name'], dict['mass'])
        self.id = uuid.uuid4()
        # self.name = dict['name']
        # self.mass = dict['mass']
        # self.damage = dict['damage']
        self.hands = dict['hands']
        self.price = dict['price']
        # self.quality = dict['quality']
        self.is_hidden = dict['is_hidden']
        self.dices = dict['dices']
        self.dice_type = dict['dice_type']
    
    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'hands': self.hands,
            'price': self.price,
            'is_hidden': self.is_hidden,
            'dices': self.dices,
            'dice_type': self.dice_type,
        }
