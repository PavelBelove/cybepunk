import rich


from rich import print
from enum import Enum
from core.classes.character.life_path_enums import LifePath
from core.utils.dises import get_random_d10, get_random_d6


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
    def __init__(self, name, role, stats: Stats, skills: Skills, life_path: LifePath) -> None:
        super().__init__(name)
        self._role = role
        self._skills = skills
        self._life_path = life_path
        self._stats = stats
        self._hit_points = hit_points_dict[f'{self._stats._body}']['initial_hit_points']
        self._max_hit_points = hit_points_dict[f'{self._stats._body}']['initial_hit_points']
        self._left_hand_weapon = None
        self._right_hand_weapon = None
        self._inventory = {}

    def set_weapon(self, right_hand_weapon, left_hand_weapon=None):
        # add logic for two-handed weapons
        self._right_hand_weapon = right_hand_weapon
        self._left_hand_weapon = left_hand_weapon

    def attack(
        self,
        enemy,
        weapon,
        dice_enemy: int,

    ) -> int:
        if isinstance(weapon, Guns):
            weapon_skills = self._skills._marksmanship
        elif isinstance(weapon, MeleeWeapon):
            weapon_skills = self._skills._melee_weapon
        else:
            weapon_skills = self._skills._athletics

        dices = []
        for i in range(weapon.dices):
            if weapon.dice_type == 6:
                dices.append(get_random_d6())
            else:
                dices.append(get_random_d10())

        character_damage = self._stats._dex + weapon_skills + sum(dices)
        enemy_defence = enemy._stats._dex + enemy._skills._evasion + dice_enemy

        print('Your dices is', *dices)
        print('#####: ', character_damage, enemy_defence)

        return character_damage if character_damage > enemy_defence else 0
    
    def as_json(self):
        return {
            'role': self._role,
            'skills': self._skills.as_json(),
            'life_path': self._life_path.as_json(),
            'stats': self._stats.as_json(),
            'hit_points': self._hit_points,
            'max_hit_points': self._max_hit_points,
            'left_hand_weapon': self._left_hand_weapon.as_json(),
            'right_hand_weapon': self._right_hand_weapon.as_json(),
            # TODO: 'inventory': self._inventory,
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
