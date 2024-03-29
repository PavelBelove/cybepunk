import json

from core.factories.character.character_factory import CharacterFactory
from core.factories.character.life_path_factory import LifePathFactory
from core.factories.stats_factory import StatsFactory
from core.factories.weapon.weapon_factory import WeaponFactory
from core.factories.weapon.guns_factory import GunFactory
from core.factories.weapon.melee_weapon_factory import MeleeWeaponFactory


from core.character_data.stats.stat_presets import STATS_PRESETS
from character.models import Character, LifePath, Skills, Stats
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.forms import model_to_dict
from random import choice, randint
from rich import print


User = get_user_model()


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
    character_factory = CharacterFactory(
        stats_factory, life_path_factory, weapon_factory)
    core_character = character_factory.create_random_character(name, role)
    dict_character = core_character.as_json()

    # создание моделей для character

    stats_new = Stats.objects.create(
        intel=dict_character['stats']['intel'],
        ref=dict_character['stats']['ref'],
        dex=dict_character['stats']['dex'],
        tech=dict_character['stats']['tech'],
        cool=dict_character['stats']['cool'],
        will=dict_character['stats']['will'],
        lusk=dict_character['stats']['lusk'],
        move=dict_character['stats']['move'],
        body=dict_character['stats']['body'],
        emp=dict_character['stats']['emp'],
    )

    skills_new = Skills.objects.create(
        brawling=dict_character['skills']['brawling'],
        evasion=dict_character['skills']['evasion'],
        marksmanship=dict_character['skills']['marksmanship'],
        melee_weapon=dict_character['skills']['melee_weapon'],
        concentration=dict_character['skills']['concentration'],
        perception=dict_character['skills']['perception'],
        tracking=dict_character['skills']['tracking'],
        driving=dict_character['skills']['driving'],
        athletics=dict_character['skills']['athletics'],
        stealth=dict_character['skills']['stealth'],
        basic_tech=dict_character['skills']['basic_tech'],
        cybertech=dict_character['skills']['cybertech'],
        first_aid=dict_character['skills']['first_aid'],
        play_instrument=dict_character['skills']['play_instrument'],
        education=dict_character['skills']['education'],
        local_expert=dict_character['skills']['local_expert'],
        bribery=dict_character['skills']['bribery'],
        conversation=dict_character['skills']['conversation'],
        human_perception=dict_character['skills']['human_perception'],
        interrogation=dict_character['skills']['interrogation'],
        persuasion=dict_character['skills']['persuasion'],
    )

    life_path_new = LifePath.objects.create(
        family=dict_character['life_path']['family'],
        motivation=dict_character['life_path']['motivation'],
        goals=dict_character['life_path']['goals'],
        friends=dict_character['life_path']['friends'],
        enemies=dict_character['life_path']['enemies'],
        romance=dict_character['life_path']['romance'],
        personality=dict_character['life_path']['personality'],
    )

    ROLES = {
        'FIXER': 1,
        'ROCKERBOY': 2,
        'SOLO': 3,
        'NETRUNNER': 4,
        'NOMAD': 5,
        'TECH': 6,
        'COP': 7,
        'CORPORATE': 8,
        'MEDIC': 9,
        'JOUNALIST': 10,
    }

    character_new = Character.objects.create(
        user=User.objects.first(),  # Сделать получение текущего пользователя
        name=dict_character['name'],
        role=ROLES[dict_character['role'].upper()],
        skills=skills_new,
        life_path=life_path_new,
        stats=stats_new,
        hit_points=dict_character['hit_points'],
        max_hit_points=dict_character['max_hit_points'],
        left_hand_weapon=dict_character['left_hand_weapon'],
        right_hand_weapon=dict_character['right_hand_weapon'],
        inventory=dict_character['inventory'],
    )

    return core_character.as_json()
    # return stats_new.as_json()


if __name__ == '__main__':
    pass
