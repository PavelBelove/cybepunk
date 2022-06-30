import random
from re import I

from classes.character.skills import Skills
from character_data.skill_examples import skill_examples


class Character:
    def __init__(self, name, role, intel, ref, dex, tech, cool, will, lusk, move, body, emp, extra_skills) -> None:
        self._name = name
        self._role = role
        self._intel = intel
        self._ref = ref
        self._dex = dex
        self._tech = tech
        self._cool = cool
        self._will = will
        self._lusk = lusk
        self._move = move
        self._body = body
        self._emp = emp

        self.Skills = Skills(
            # Fighting Skills
            _brawling=self._dex + extra_skills['brawling'],
            _evasion=self._dex + extra_skills['evasion'],
            _marksmanship=self._ref + extra_skills['marksmanship'],
            _melee_weapon=self._dex + extra_skills['melee_weapon'],
            # Awareness Skills
            _concentration=self._will + extra_skills['concentration'],
            _perception=self._intel + extra_skills['perception'],
            _tracking=self._intel + extra_skills['tracking'],
            # Control Skills
            _driving=self._ref + extra_skills['driving'],
            # Body Skills
            _athletics=self._dex + extra_skills['athletics'],
            _stealth=self._emp + extra_skills['stealth'],
            # Technique Skills
            _basic_tech=self._tech + extra_skills['basic_tech'],
            _cybertech=self._tech + extra_skills['cybertech'],
            _first_aid=self._tech + extra_skills['first_aid'],
            # Performance_skills
            _play_instrument=self._emp + extra_skills['play_instrument'],
            # Education Skills
            _education=self._intel + extra_skills['education'],
            _local_expert=self._intel + extra_skills['local_expert'],
            # Social Skills
            _bribery=self._cool + extra_skills['bribery'],
            _conversation=self._emp + extra_skills['conversation'],
            _human_perception=self._emp + extra_skills['human_perception'],
            _interrogation=self._cool + extra_skills['interrogation'],
            _persuasion=self._cool + extra_skills['persuasion'],
        )

    # getter methods

    def get_name(self):
        return self._name

    def get_role(self):
        return self._role

    def get_intel(self):
        return self._intel

    def get_ref(self):
        return self._ref

    def get_dex(self):
        return self._dex

    def get_tech(self):
        return self._tech

    def get_cool(self):
        return self._cool

    def get_will(self):
        return self._will

    def get_lusk(self):
        return self._lusk

    def get_move(self):
        return self._move

    def get_body(self):
        return self._body

    def get_emp(self):
        return self._emp

# setter method

    def set_name(self, new_name):
        self._name = new_name
        return self._name

    def set_role(self, new_role):
        self._role = new_role
        return self._role

    def set_intel(self, new_intel):
        self._intel = new_intel
        return self._intel

    def set_ref(self, new_ref):
        self._ref = new_ref
        return self._ref

    def set_dex(self, new_dex):
        self._dex = new_dex
        return self._dex

    def set_tech(self, new_tech):
        self._tech = new_tech
        return self._tech

    def set_cool(self, new_cool):
        self._cool = new_cool
        return self._cool

    def set_will(self, new_will):
        self._will = new_will
        return self._will

    def set_lusk(self, new_lusk):
        self._lusk = new_lusk
        return self._lusk

    def set_move(self, new_move):
        self._move = new_move
        return self._move

    def set_body(self, new_body):
        self._body = new_body
        return self._body

    def set_emp(self, new_emp):
        self._emp = new_emp
        return self._emp


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
