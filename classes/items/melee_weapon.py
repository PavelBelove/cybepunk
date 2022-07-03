
from enum import Enum
from classes.items.weapon import Weapon, WeaponType

# _________________
import random


def uniqueid():
    seed = random.getrandbits(32)
    while True:
        yield seed
        seed += 1


uid = uniqueid()
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
        'name': 'knife',
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


class MeleeWeapon(Weapon):
    def __init__(self, dict):
        super().__init__(dict)


# knifes = [MeleeWeapon(knifes_data[knife]) for knife in knifes_data]

# print(knifes)

# knife = MeleeWeapon(knifes_data['knife'])
# print(knife)
