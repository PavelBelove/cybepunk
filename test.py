from enum import Enum
# from classes.weapon import Weapon, WeaponType

# _________________
import random


def _uniqueid():
    seed = random.getrandbits(32)
    while True:
        yield seed
        seed += 1


uid = _uniqueid()
# _________________

knifes_data = {
    'small_knife': {
        'id': uid,
        'name': 'small_knife',
        'mass': 'light',
        # 'damage': '',
        'hands': 1,
        'price': 10,
        # 'quality': '',
        'is_hidden': True,
        'dices': 2,
        'dice_type': 6,
    },
    'knife': {
        'id': uid,
        'name': 'small_knife',
        'mass': 'light',
        # 'damage': '',
        'hands': 1,
        'price': 10,
        # 'quality': '',
        'is_hidden': True,
        'dices': 2,
        'dice_type': 6,
    },
    'machete': {
        'id': uid,
        'name': 'machete',
        'mass': 'middle',
        # 'damage': '',
        'hands': 1,
        'price': 20,
        # 'quality': '',
        'is_hidden': False,
        'dices': 3,
        'dice_type': 6,
    }
}


# class MeleeWeaponType(WeaponType):
#     SMALL_KNIFE = 0
#     KNIFE = 1
#     MACHETE = 2


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


class MeleeWeapon(Weapon):
    def __init__(self, dict):
        super().__init__(dict)


for i in range(10):
    knife = MeleeWeapon(knifes_data['knife'])
    small_knife = MeleeWeapon(knifes_data['small_knife'])
    print(knife.id, small_knife.id)
