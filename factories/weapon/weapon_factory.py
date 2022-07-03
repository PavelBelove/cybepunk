from factories.weapon.melee_weapon_factory import MeleeWeaponFactory, MeleeWeaponType
from factories.weapon.guns_factory import GunFactory, GunType
from classes.character.character import Role


class WeaponFactory():
    def __init__(
        self,
        melee_weapon_factory: MeleeWeaponFactory,
        gun_factory: GunFactory,
    ):
        self._melee_weapon_factory = melee_weapon_factory
        self._gun_factory = gun_factory

    def _create_preset_weapons_for_role(role: Role):
        if (role == Role.FIXER):
            slice_and_dice = self._melee_weapon_factory.create(
                MeleeWeaponType.SLICE_AND_DICE)
            heavy_pistol = self._gun_factory.create(GunType.HEAVY_PISTOL)
            return [slice_and_dice, heavy_pistol]

        return []

    def create_fixer_weapons():
        self._create_weapons_for_class(Role.FIXER)
