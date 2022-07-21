
from enum import Enum


# from random_gen.id_generator import unique_sequence
from classes.character.character import Role
from classes.items.weapon import Weapon
from classes.items.guns import Guns
from character_data_out.weapons.guns import pistol_data, ammo_pistol_data

# Это такая модель пистолета


class Pistol(Guns):
    def __init__():
        pass


# Это модель пистолета
class HeavyPistol(Guns):
    def __init__(
            self,
            pistol_dict=pistol_data['heavy_pistol'],
            ammo_dict=ammo_pistol_data['ammo_heavy_pistol']):
        super().__init__(pistol_dict, ammo_dict)
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


if __name__ == '__main__':
    pistol = GunFactory.create(GunType.HEAVY_PISTOL)
    # pistol = HeavyPistol()
    print(pistol.__dict__)
    # print(pistol_data['heavy_pistol'])
