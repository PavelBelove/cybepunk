# from factories.weapon.weapon_factory import WeaponFactory
from random import choice

from core.character_data.armor_presets import ARMOR_PRESETS
from core.character_data.items.inventory_presets import ITEMS_PRESETS
from core.character_data.names import NAMES
from core.classes.character.character import Character
from core.classes.character.skills import Skills
from core.character_data import skill_examples
from core.factories.item.armor_factory import ArmorFactory
from core.factories.character.life_path_factory import LifePathFactory
from core.factories.stats_factory import StatsFactory
from core.factories.item.item_factory import ItemFactory
# from core.factories.weapon.weapon_factory import WeaponFactory
# from core.factories.weapon.melee_weapon_factory import MeleeWeaponFactory, MeleeWeaponType
# from core.factories.weapon.guns_factory import GunFactory, GunType


class CharacterFactory:
    @staticmethod
    def build_character_factory():
        stats_factory = StatsFactory()
        # melee_weapon_factory = MeleeWeaponFactory()
        # gun_factory = GunFactory()
        # weapon_factory = WeaponFactory(
        #     melee_weapon_factory,
        #     gun_factory
        # )
        life_path_factory = LifePathFactory()
        item_factory = ItemFactory()
        armor_factory = ArmorFactory()
        character_factory = CharacterFactory(
            stats_factory,
            life_path_factory,
            item_factory,
            armor_factory
        )

        return character_factory

    def __init__(
        self,
        stats_factory: StatsFactory,
        life_path_factory: LifePathFactory,
        item_factory: ItemFactory,
        armor_factory=ArmorFactory
    ):
        self._stats_factory = stats_factory
        self._item_factory = item_factory
        self._armor_factory = armor_factory
        self._life_path_factory = life_path_factory

    def _create_inventory(self, inventory_preset):
        inventory = []
        for i in inventory_preset:
            inventory.append(self._item_factory.create_item(i))
        return inventory

    def _create_skills(self, stats):
        skills = Skills(
            # Fighting Skills
            _brawling=stats._dex + \
            skill_examples.skill_examples['FIXER']['brawling'],
            _evasion=stats._dex + \
            skill_examples.skill_examples['FIXER']['evasion'],
            _marksmanship=stats._ref + \
            skill_examples.skill_examples['FIXER']['marksmanship'],
            _melee_weapon=stats._dex + \
            skill_examples.skill_examples['FIXER']['melee_weapon'],
            # Awareness Skills
            _concentration=stats._will + \
            skill_examples.skill_examples['FIXER']['concentration'],
            _perception=stats._intel + \
            skill_examples.skill_examples['FIXER']['perception'],
            _tracking=stats._intel + \
            skill_examples.skill_examples['FIXER']['tracking'],
            # Control Skills
            _driving=stats._ref + \
            skill_examples.skill_examples['FIXER']['driving'],
            # Body Skills
            _athletics=stats._dex + \
            skill_examples.skill_examples['FIXER']['athletics'],
            _stealth=stats._emp + \
            skill_examples.skill_examples['FIXER']['stealth'],
            # Technique Skills
            _basic_tech=stats._tech + \
            skill_examples.skill_examples['FIXER']['basic_tech'],
            _cybertech=stats._tech + \
            skill_examples.skill_examples['FIXER']['cybertech'],
            _first_aid=stats._tech + \
            skill_examples.skill_examples['FIXER']['first_aid'],
            # Performance_skills
            _play_instrument=stats._emp + \
            skill_examples.skill_examples['FIXER']['play_instrument'],
            # Education Skills
            _education=stats._intel + \
            skill_examples.skill_examples['FIXER']['education'],
            _local_expert=stats._intel + \
            skill_examples.skill_examples['FIXER']['local_expert'],
            # Social Skills
            _bribery=stats._cool + \
            skill_examples.skill_examples['FIXER']['bribery'],
            _conversation=stats._emp + \
            skill_examples.skill_examples['FIXER']['conversation'],
            _human_perception=stats._emp + \
            skill_examples.skill_examples['FIXER']['human_perception'],
            _interrogation=stats._cool + \
            skill_examples.skill_examples['FIXER']['interrogation'],
            _persuasion=stats._cool + \
            skill_examples.skill_examples['FIXER']['persuasion'],
        )
        return skills

    def create_character(self, name, role, stats, life_path, inventory, armor):
        return Character(
            name,
            role,
            stats,

            self._create_skills(
                stats if stats else skill_examples.skill_examples['FIXER']),
            life_path,
            inventory,
            armor
        )

    # def create_random_fixer(self, name, stats=None, life_path=None):
    #     stats = stats if stats is not None else self._stats_factory._create_preset_stats('FIXER',
    #                                                                                      1)
    #     life_path = life_path if life_path is not None else self._life_path_factory.create()
    #     fixer = self.create_character(
    #         name,
    #         'Fixer',
    #         stats,
    #         life_path,
    #         # skills if skills else,
    #     )

    #     # FIXME: Fix DRY

    #     slice_and_dice = self._weapon_factory.create(
    #         MeleeWeaponType.SLICE_AND_DICE)
    #     heavy_pistol = self._weapon_factory.create(GunType.HEAVY_PISTOL)

    #     fixer._inventory[slice_and_dice.id] = slice_and_dice
    #     fixer._inventory[heavy_pistol.id] = heavy_pistol

    #     fixer.set_weapon(
    #         slice_and_dice,
    #         heavy_pistol
    #     )

    #     return fixer

    def create_random_character(self, name=None, role=None, stats=None, life_path=None, inventory=None, armor=None):
        name = name if name is not None else choice(NAMES)
        role = role if role is not None else choice((
            'FIXER',
            'ROCKERBOY',
            'SOLO',
            'NETRUNNER',
            'NOMAD',
            'TECH',
        ))
        stats = stats if stats is not None else self._stats_factory._create_preset_stats(role,
                                                                                         1)
        life_path = life_path if life_path is not None else self._life_path_factory.create()
        inventory = inventory if inventory is not None else self._create_inventory(
            ITEMS_PRESETS[role])
        armor = armor if armor is not None else self._armor_factory.create_armor(
            ARMOR_PRESETS[role])
        character = self.create_character(
            name,
            role,
            stats,
            life_path,
            inventory,
            armor
            # skills if skills else,
        )

        # FIXME: Fix DRY

        # slice_and_dice = self._weapon_factory.create(
        #     MeleeWeaponType.SLICE_AND_DICE)
        # heavy_pistol = self._weapon_factory.create(GunType.HEAVY_PISTOL)

        # character._inventory[slice_and_dice.id] = slice_and_dice
        # character._inventory[heavy_pistol.id] = heavy_pistol

        # character.set_weapon(
        #     slice_and_dice,
        #     heavy_pistol
        # )

        return character


if __name__ == '__main__':
    stats_factory = StatsFactory()
    melee_weapon_factory = MeleeWeaponFactory()
    life_path_factory = LifePathFactory()
    gun_factory = GunFactory()
    weapon_factory = WeaponFactory(melee_weapon_factory, gun_factory)
    character_factory = CharacterFactory(
        stats_factory, life_path_factory, weapon_factory)

    fixer = character_factory.create_random_fixer('name')
    # print(fixer.__dict__.keys())
    print('STATS:    ', fixer._stats.__dict__)
    print('SKILLS:   ', fixer._skills.__dict__)
    print('LIFE PATH:   ', fixer._life_path.__dict__)

    print(fixer._right_hand_weapon.__dict__)
