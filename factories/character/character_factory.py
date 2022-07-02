from random import randint

from factories.weapon.melee_weapon_factory import MeleeWeaponFactory, MeleeWeaponType
from classes.character.character import Character
from classes.character.stats import Stats
from classes.character.skills import Skills
from character_data import life_path_rus, skill_examples
from factories.stats_factory import StatsFactory


def _get_random_d10(upperValue):
    return randint(1, 11)


def _get_random_d6(upperValue):
    return randint(1, 11)


class CharacterFactory:
    def __init__(self, stats_factory: StatsFactory, weapon_factory: MeleeWeaponFactory):
        self._stats_factory = stats_factory
        self._weapon_factory = weapon_factory

        # For Rocker

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

    def create_character(self, name, role, stats):
        return Character(
            name,
            role,
            stats,
            self._create_skills(
                stats if stats else skill_examples.skill_examples['FIXER'])
        )

    def create_random_fixer(self, name, stats=None):
        stats = stats if stats != None else self._stats_factory._create_preset_stats('FIXER',
                                                                                     1)
        fixer = self.create_character(
            name,
            'Fixer',
            stats,
            # skills if skills else,
        )

        weapon = self._weapon_factory.create(MeleeWeaponType.SMALL_KNIFE)

        fixer.set_weapon(weapon)
        return fixer
