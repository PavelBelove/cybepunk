from operator import ge
from webbrowser import get
import rich


from rich import print
from enum import Enum
from core.classes.items.armor import Armor
from core.classes.character.life_path_enums import LifePath
from core.utils.dises import get_random_d10, get_random_d6

from core.character_data.items.item_options import ITEM_TYPE, IMPLANT_SLOTS, MASS, HANDS

from core.classes.character.skills import Skills
from core.classes.character.stats import Stats
from core.classes.character.life_path import LifePath
from core.classes.items.melee_weapon import MeleeWeapon
from core.classes.items.guns import Guns
from core.character_data.skill_examples import skill_examples
from core.character_data.stats.hit_points import hit_points_dict


class Role(Enum):
    FIXER = 'FIXER'
    ROCKERBOY = 'ROCKERBOY'
    SOLO = 'SOLO'
    NETRUNNER = 'NETRUNNER'
    NOMAD = 'NOMAD'
    TECH = 'TECH'
    COP = 'COP'
    CORPORATE = 'CORPORATE'
    MEDIC = 'MEDIC'
    JOUNALIST = 'JOUNALIST'


class Actor:
    def __init__(self, name, hit_points=20, max_hit_points=20):
        self._name = name
        self._hit_points = hit_points
        self._max_hit_points = max_hit_points


class Character(Actor):
    def __init__(self, name, role, stats: Stats, skills: Skills, life_path: LifePath, inventory: list, armor: Armor) -> None:
        super().__init__(name)
        self._role = role
        self._skills = skills
        self._life_path = life_path
        self._stats = stats
        self._hit_points = hit_points_dict[f'{self._stats._body}']['initial_hit_points']
        self._max_hit_points = hit_points_dict[f'{self._stats._body}']['initial_hit_points']
        # self._left_hand_weapon = None
        # self._right_hand_weapon = None
        self._inventory = inventory
        self._armor = armor

    def skill_test(self, skill, complexity):
        character_skill = self._skills[skill]
        d10 = get_random_d10()
        if d10 == 10:
            critical_result = 'Критический успех'
            d10 += get_random_d10()
        elif d10 == 1:
            critical_result = 'Критическая неудача'
        else:
            critical_result = ''

        skill_test = True if character_skill + d10 >= complexity else False

        skill_test_report = {
            'character_skill': character_skill,
            'd10': d10,
            'skill_test': skill_test,
            'critical_result': critical_result
        }

        return skill_test_report

    def throw_initiative_dice(self):
        '''Initiative = REF + 1d10'''
        return self._stats._ref + get_random_d10()

    def attack(
        self,
        enemy,
        weapon,
        dice_enemy: int,
    ) -> int:
        if weapon.item_type == 2:  # Gun
            weapon_skills = self._skills._marksmanship
        elif weapon.item_type == 1:  # Melee
            weapon_skills = self._skills._melee_weapon
        else:
            weapon_skills = self._skills._athletics

        dices = []
        for i in range(weapon.dices):
            if weapon.dice_type == 6:
                dices.append(get_random_d6())
            else:
                dices.append(get_random_d10())

        # Сделать выбор голова или тело для атаки
        d10_character = get_random_d10()
        if d10_character == 10:
            critical_result = 'Критический успех'
            d10_character += get_random_d10()
        elif d10_character == 1:
            critical_result = 'Критическая неудача'
        else:
            critical_result = ''

        character_damage = weapon_skills + sum(dices) - enemy._armor.body
        character_accuracy = weapon_skills + d10_character
        enemy_defence = enemy._skills._evasion + dice_enemy

        attack_report = {
            'd10_enemy': dice_enemy,
            'd10_character': d10_character,
            'd6_dices': dices,
            'character_damage': character_damage,
            'character_accuracy': character_accuracy,
            'enemy_defence': enemy_defence,
            'critical_result': critical_result
        }

        if character_accuracy > enemy_defence:
            enemy._armor.body -= 1
            enemy._hit_points = int(enemy._hit_points) - character_damage
            attack_report['damage'] = character_damage
        else:
            attack_report['damage'] = 0

        attack_report['enemy_hit_points'] = int(enemy._hit_points)

        return attack_report

    def as_json(self):
        return {
            'name': self._name,
            'role': self._role,
            'skills': self._skills.as_json(),
            'life_path': self._life_path.as_json(),
            'stats': self._stats.as_json(),
            'hit_points': self._hit_points,
            'max_hit_points': self._max_hit_points,
            # 'left_hand_weapon': self._left_hand_weapon.as_json(),
            # 'right_hand_weapon': self._right_hand_weapon.as_json(),
            'inventory': [item.as_json() for item in self._inventory.values()],
            'armor': self._armor.as_json(),
        }


if __name__ == '__main__':
    aktor = Character('Greese', 'FIXER', )

    # print(
    #     'Имя', security_guard.get_name(), '\n',
    #     'Роль', security_guard.get_role(), '\n',
    #     'Интеллект', security_guard.get_intel(), '\n',
    #     'Реакция', security_guard.get_ref(), '\n',
    #     'Ловость', security_guard.get_dex(), '\n',
    #     'Техника', security_guard.get_tech(), '\n',
    #     'Крутость', security_guard.get_cool(), '\n',
    #     'Харизма', security_guard.get_will(), '\n',
    #     'Воля', security_guard.get_lusk(), '\n',
    #     'Скорость', security_guard.get_move(), '\n',
    #     'Тело', security_guard.get_body(), '\n',
    #     'Эмпатия', security_guard.get_emp(), '\n',
    #     'brawling', security_guard.Skills.get_brawling(), '\n',
    # )
