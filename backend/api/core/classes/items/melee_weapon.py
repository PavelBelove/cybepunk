
from enum import Enum
from core.classes.items.weapon import Weapon, WeaponType


class MeleeWeapon(Weapon):
    def __init__(self, dict):
        super().__init__(dict)
