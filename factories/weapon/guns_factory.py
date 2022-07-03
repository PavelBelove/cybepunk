
from enum import Enum


# from random_gen.id_generator import unique_sequence
from classes.character.character import Role
from classes.weapons.weapon import Weapon
from character_data.weapons.guns import pistol_data, ammo_pistol_data

# Это такая модель пистолета


class Pistol(Guns):
    def __init__():
        pass


# Это модель пистолета
class HeavyPistol(Guns):
    def __init__(
            self,
            pistol_dict=pistol_data['heave_pistol'],
            ammo_dict=ammo_pistol_data['ammo_heavy_pistol']):
        super().__init__(pistol_dict)
        self.ammo = ammo_dict


class GunType(Enum):
    HEAVY_PISTOL = 'HEAVY_PISTOL'


class GunFactory():
    def __init__(self) -> None:
        pass

    def create(self, gun_type: GunType):
        gun_classes = {
            GunType.HEAVY_PISTOL: HeavyPistol,
        }

        return gun_classes[gun_type]()
