import json

from core.factories.character.character_factory import CharacterFactory
from core.character_data.stats.stat_presets import STATS_PRESETS
from character.models import Character, LifePath, Skills, Stats, Weapon
from django.http import HttpResponse, JsonResponse
from django.forms import model_to_dict
from random import choice, randint
from rich import print


# from character_data.stats.stat_presets import STATS_PRESETS
# from character.character_data.life_path_rus import FAMILY, MOTIVATION, GOALS, FRIENDS, ENEMIES, ROMANCE, PERSONALITY
# from classes.character.life_path_enums import Family


def preset_stats(role_presets, dispersion=0):
    '''
    Выдает случайные статы из пресета согласно роли.
    dispersion - случайные отклонения от пресета 
    Значения более 10 и менее 3 заменяются 10 и 3 соответственно
    '''

    def modified_stat(stat, dispersion=dispersion):
        '''Случайные отклонения'''
        modified_stat = stat + randint(-dispersion, dispersion)
        if modified_stat > 10:
            return 10
        elif modified_stat < 3:
            return 3
        return modified_stat

    preset = STATS_PRESETS['FIXER'][choice(list(STATS_PRESETS["FIXER"]))]

    stats = {
        'intel': modified_stat(preset['intelligence']),
        'ref': modified_stat(preset['reflexes']),
        'dex': modified_stat(preset['agility']),
        'tech': modified_stat(preset['tech']),
        'cool': modified_stat(preset['cool']),
        'will': modified_stat(preset['will']),
        'lusk': modified_stat(preset['luck']),
        'move': modified_stat(preset['movement']),
        'body': modified_stat(preset['body']),
        'emp': modified_stat(preset['empathy']),
    }

    print(preset)
    return stats  # json.dumps(stats)


def preset_life_path():
    '''
    Генерация жизненного пути персонажа
    '''
    print()


def preset_character(name, role, dispersion=0):
    '''
    Генерирует случайного персонажа из пресетов.
    '''
    stats = preset_stats(role, dispersion=dispersion)
    new_stats = Stats.objects.create(
        intel=stats['intel'],
        ref=stats['ref'],
        dex=stats['dex'],
        tech=stats['tech'],
        cool=stats['cool'],
        will=stats['will'],
        lusk=stats['lusk'],
        move=stats['move'],
        body=stats['body'],
        emp=stats['emp'],
    )
    new_stats.save()

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

    core_character_data = CharacterFactory.create_character()

    character = core_character_data

    return character


if __name__ == '__main__':
    # print(preset_stats(STATS_PRESETS['FIXER'], 0))
    print(FAMILY[Family])
