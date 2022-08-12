
from core.character_data.armor_presets import ARMOR_PRESETS

from core.factories.character.character_factory import CharacterFactory
from core.factories.character.life_path_factory import LifePathFactory
from core.factories.stats_factory import StatsFactory
from core.factories.weapon.weapon_factory import WeaponFactory
from core.factories.weapon.guns_factory import GunFactory
from core.factories.weapon.melee_weapon_factory import MeleeWeaponFactory


from core.character_data.stats.stat_presets import STATS_PRESETS
from core.character_data.items.inventory_presets import ITEMS_PRESETS
from character.models import Armor, Character, ImplantSlots, Items, LifePath, Skills, Stats
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.forms import model_to_dict
from random import choice, randint
from rich import print


User = get_user_model()

preset_inventory = [
    {
        'name': 'small_knife',
        'weight': 1,
        # 'damage': '',
        'hands': 1,
        'price': 10,
        # 'quality': '',
        'is_hidden': True,
        'dices': 3,
        'dice_type': 6,
    },
    {
        'name': 'machete',
        'weight': 1,
        # 'damage': '',
        'hands': 1,
        'price': 20,
        # 'quality': '',
        'is_hidden': False,
        'dices': 3,
        'dice_type': 6,
    },
    {
        'name': 'Slice And Dice',
        'weight': 0,
        # 'damage': '',
        'hands': 1,
        'price': 20,
        # 'quality': '',
        'is_hidden': False,
        'dices': 2,
        'dice_type': 6,
    }
]


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

    # print(preset)
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

    def create_item(character_id, **item):
        item = Items.objects.create(
            character_id=character_id,
            **item
        )

        return item.as_json()

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

    ROLES = {
        'FIXER': 'FIXER',
        'ROCKERBOY': 'ROCKERBOY',
        'SOLO': 'SOLO',
        'NETRUNNER': 'NETRUNNER',
        'NOMAD': 'NOMAD',
        'TECH': 'TECH',
        'COP': 'COP',
        'CORPORATE': 'CORPORATE',
        'MEDIC': 'MEDIC',
        'JOUNALIST': 'JOUNALIST',
    }

    character_new = Character.objects.create(
        user=User.objects.first(),  # Сделать получение текущего пользователя
        name=dict_character['name'],
        role=ROLES[dict_character['role'].upper()],
        # skills=skills_new,
        # life_path=life_path_new,
        # stats=stats_new,
        hit_points=dict_character['hit_points'],
        max_hit_points=dict_character['max_hit_points'],
        left_hand_weapon=dict_character['left_hand_weapon'],
        right_hand_weapon=dict_character['right_hand_weapon'],
        # inventory=dict_character['inventory'],
    )

    inventory = [create_item(character_new.id, **item)
                 for item in ITEMS_PRESETS[role]]

    stats_new = Stats.objects.create(
        character_id=character_new.id,
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
        character_id=character_new.id,
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
        character_id=character_new.id,
        family=dict_character['life_path']['family'],
        motivation=dict_character['life_path']['motivation'],
        goals=dict_character['life_path']['goals'],
        friends=dict_character['life_path']['friends'],
        enemies=dict_character['life_path']['enemies'],
        romance=dict_character['life_path']['romance'],
        personality=dict_character['life_path']['personality'],
    )

    def install_implants_presets(inventory=inventory):
        slots = {}
        for item in inventory:
            if item.get('installed'):
                slots[item['slot']] = Items.objects.get(id=item['item_id'])
        return slots

    implant_slots_new = ImplantSlots.objects.create(
        character_id=character_new.id, **install_implants_presets()
    )

    armor_new = Armor.objects.create(
        character_id=character_new.id,
        head_level=ARMOR_PRESETS[role]['head'],
        head_wear=ARMOR_PRESETS[role]['head_wear'],
        body_level=ARMOR_PRESETS[role]['body'],
        body_wear=ARMOR_PRESETS[role]['body_wear'],
    )

    return character_new.as_json()


if __name__ == '__main__':
    pass
