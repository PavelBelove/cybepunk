from calendar import c
from enum import Enum

from classes.weapons.melee_weapon import MeleeWeapon, knifes_data
# from random_gen.id_generator import unique_sequence


class MeleeWeaponType(Enum):
    SMALL_KNIFE = 0
    KNIFE = 1
    MACHETE = 2


class SmallKnife(MeleeWeapon):
    def __init__(self, dict=knifes_data['small_knife']):
        super().__init__(dict)


class Knife(MeleeWeapon):
    def __init__(self, dict=knifes_data['knife']):
        super().__init__(dict)


class Machete(MeleeWeapon):
    def __init__(self, dict=knifes_data['machete']):
        super().__init__(dict)


class CreateMeleeWeapon():
    def __init__(self) -> None:
        pass

    def create(weapon_type: MeleeWeaponType):
        factory_dict = {
            MeleeWeaponType.SMALL_KNIFE: SmallKnife,
            MeleeWeaponType.KNIFE: Knife,
            MeleeWeaponType.MACHETE: Machete,
        }
        # print(factory_dict[MeleeWeaponType.KNIFE])
        return factory_dict[weapon_type]()


if __name__ == '__main__':
    for i in MeleeWeaponType:
        weapon = CreateMeleeWeapon.create(i)

        print(f'{weapon.name}, id {weapon.id} ')
