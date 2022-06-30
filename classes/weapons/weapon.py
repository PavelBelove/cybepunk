from enum import Enum


class WeaponType(Enum):
    pass


class Weapon():
    def __init__(self, dict):
        self.id = next(dict['id'])
        self.name = dict['name']
        self.mass = dict['mass']
        # self.damage = dict['damage']
        self.hands = dict['hands']
        self.price = dict['price']
        # self.quality = dict['quality']
        self.is_hidden = dict['is_hidden']
        self.dices = dict['dices']
        self.dice_type = dict['dice_type']
