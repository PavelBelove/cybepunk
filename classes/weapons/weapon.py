from enum import Enum
import uuid


class Weight(Enum):
    light = 1
    medium = 2
    heavy = 3


class Item():
    def __init__(self, name, mass: Weight = Weight.medium):
        self.id = uuid.uuid4()
        self.name = name
        self.mass = mass


class WeaponType(Enum):
    pass


class Weapon(Item):
    def __init__(self, dict):
        super().__item__(dict['name'], 2)
        # self.damage = dict['damage']
        self.hands = dict['hands']
        self.price = dict['price']
        # self.quality = dict['quality']
        self.is_hidden = dict['is_hidden']
        self.dices = dict['dices']
        self.dice_type = dict['dice_type']
