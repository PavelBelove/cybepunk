from enum import Enum

from classes.items.melee_weapon import MeleeWeapon, knifes_data


class MeleeWeaponType(Enum):
    SMALL_KNIFE = 0
    KNIFE = 1
    MACHETE = 2
    SLICE_AND_DICE = 3


class SmallKnife(MeleeWeapon):
    def __init__(self, dict=knifes_data['small_knife']):
        super().__init__(dict)


class Knife(MeleeWeapon):
    def __init__(self, dict=knifes_data['knife']):
        super().__init__(dict)


class Machete(MeleeWeapon):
    def __init__(self, dict=knifes_data['machete']):
        super().__init__(dict)


class MeleeWeaponFactory():
    def __init__(self) -> None:
        pass

    def create(self, weapon_type: MeleeWeaponType):
        melee_weapon_classes = {
            MeleeWeaponType.SMALL_KNIFE: SmallKnife,
            MeleeWeaponType.KNIFE: Knife,
            MeleeWeaponType.MACHETE: Machete,
        }
        # print(factory[MeleeWeaponType.KNIFE])
        return melee_weapon_classes[weapon_type]()


if __name__ == '__main__':
    for i in MeleeWeaponType:
        weapon = MeleeWeaponFactory.create(i)

        print(f'{weapon.name}, id {weapon.id} ')
