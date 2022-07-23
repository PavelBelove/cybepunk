import json

from core.factories.character.character_factory import CharacterFactory
from core.factories.character.life_path_factory import LifePathFactory
from core.factories.stats_factory import StatsFactory
from core.factories.weapon.weapon_factory import WeaponFactory
from core.factories.weapon.guns_factory import GunFactory
from core.factories.weapon.melee_weapon_factory import MeleeWeaponFactory


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
    # new_stats = Stats.objects.create(
    #     intel=stats['intel'],
    #     ref=stats['ref'],
    #     dex=stats['dex'],
    #     tech=stats['tech'],
    #     cool=stats['cool'],
    #     will=stats['will'],
    #     lusk=stats['lusk'],
    #     move=stats['move'],
    #     body=stats['body'],
    #     emp=stats['emp'],
    # )
    # new_stats.save()

    stats_factory = StatsFactory()
    melee_weapon_factory = MeleeWeaponFactory()
    gun_factory = GunFactory()
    weapon_factory = WeaponFactory(melee_weapon_factory, gun_factory)
    life_path_factory = LifePathFactory()
    character_factory = CharacterFactory(stats_factory, life_path_factory, weapon_factory)
    core_character = character_factory.create_random_fixer(name)

    return core_character.as_json()


if __name__ == '__main__':
    # print(preset_stats(STATS_PRESETS['FIXER'], 0))
    print(FAMILY[Family])
