import random
from random_gen.dises import get_random_d10, get_random_d6

from classes.character.skills import Skills
from classes.character.stats import Stats
from classes.weapons.melee_weapon import MeleeWeapon
from character_data.skill_examples import skill_examples


class Actor:
    def __init__(self, name, hit_points=20, max_hit_points=20):
        self._name = name
        self._hit_points = hit_points
        self._max_hit_points = max_hit_points


hit_points_dict = {
    "2": {
        "initial_hit_points": "10",
        "injury_threshold": "5",
        "death_threshold": "2",
    },
    "3": {
        "initial_hit_points": "15",
        "injury_threshold": "8",
        "death_threshold": "3",
    }, "4": {
        "initial_hit_points": "20",
        "injury_threshold": "10",
        "death_threshold": "4",
    }, "5": {
        "initial_hit_points": "25",
        "injury_threshold": "13",
        "death_threshold": "5",
    }, "6": {
        "initial_hit_points": "30",
        "injury_threshold": "15",
        "death_threshold": "6",
    }, "7": {
        "initial_hit_points": "35",
        "injury_threshold": "18",
        "death_threshold": "7",
    }, "8": {
        "initial_hit_points": "40",
        "injury_threshold": "20",
        "death_threshold": "8",
    }, "9": {
        "initial_hit_points": "45",
        "injury_threshold": "23",
        "death_threshold": "9",
    }, "10": {
        "initial_hit_points": "50",
        "injury_threshold": "25",
        "death_threshold": "10",
    }
}


class Character(Actor):
    def __init__(self, name, role, stats: Stats, skills: Skills) -> None:
        super().__init__(name)
        self._role = role
        self._skills = skills
        self._stats = stats
        self._hit_points = hit_points_dict[f'{self._stats._body}']['initial_hit_points']
        self._max_hit_points = hit_points_dict[f'{self._stats._body}']['initial_hit_points']
        self._weapon = None

    def set_weapon(self, weapon: MeleeWeapon):
        self._weapon = weapon

    def melee_attack(
        self,
        enemy,
        dice: int,
        dice_enemy: int,
        damange_dice: int,
    ) -> int:
        character_damage = self._stats._dex + self._skills._melee_weapon + dice
        enemy_defence = enemy._stats._dex + enemy._skills._evasion + dice_enemy

        print('#####: ', character_damage, enemy_defence)

        return damange_dice if character_damage > enemy_defence else 0


if __name__ == '__main__':
    def generate_random_parameters(name, role):
        parameters = [random.randint(1, 10) for i in range(10)]

        character = Character(name, role, *parameters, skill_examples['FIXER'])
        return character

    security_guard = generate_random_parameters('security', 'solo')
    security_guard.set_role('fixer')

    print(
        'Имя', security_guard.get_name(), '\n',
        'Роль', security_guard.get_role(), '\n',
        'Интеллект', security_guard.get_intel(), '\n',
        'Реакция', security_guard.get_ref(), '\n',
        'Ловость', security_guard.get_dex(), '\n',
        'Техника', security_guard.get_tech(), '\n',
        'Крутость', security_guard.get_cool(), '\n',
        'Харизма', security_guard.get_will(), '\n',
        'Воля', security_guard.get_lusk(), '\n',
        'Скорость', security_guard.get_move(), '\n',
        'Тело', security_guard.get_body(), '\n',
        'Эмпатия', security_guard.get_emp(), '\n',
        'brawling', security_guard.Skills.get_brawling(), '\n',
    )
