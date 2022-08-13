from rich import print
from random import randint

from core.factories.character.life_path_factory import LifePathFactory
from core.factories.stats_factory import StatsFactory
from core.factories.weapon.guns_factory import GunFactory
from core.factories.weapon.melee_weapon_factory import MeleeWeaponFactory
from core.factories.weapon.weapon_factory import WeaponFactory
from core.factories.character.character_factory import CharacterFactory
from core.classes.character.character import Character
from core.classes.fights.fight import Fight, Party, Location

from core.utils.dises import get_random_d10, get_random_d6


character_factory = CharacterFactory.build_character_factory()

characters = [
    character_factory.create_random_character(name="Jonh Smith", role='SOLO'),
    character_factory.create_random_character(
        name="Alan Ripley", role='FIXER'),
    character_factory.create_random_character(
        name="Jonh Cohnor", role='FIXER'),
]

enemies = [
    character_factory.create_random_character(
        name="Alan Silverstry", role='FIXER'),
    character_factory.create_random_character(
        name="Michael Mc Cann", role='FIXER'),
    character_factory.create_random_character(
        name="John Travolta", role='FIXER'),
]

party = Party(characters)
enemies_party = Party(enemies)

location = Location("warehouse")
fight = Fight(location, party, enemies_party)

CHOOSE_ACTION_TEXT = '\nВыберите действие: \n1. Атака\n2. Перемещение\n'
CHOOSE_WEAPON_TEXT = '\nВыберите оружие: \n'
CHOOSE_TARGET = '\nВыберите цель: \n'

ACTION_CHOICE = 1
MOVE_CHOICE = 2
EQUIP_CHOICE = 3


def get_character_weapons_list(character):
    return [item for item in character._inventory if item.get('in_hands')]


def get_character_weapons_choices_text(weapons_list):
    return [f'{idx}. {weapon["name"]}. Dice: {weapon["dices"]}d{weapon["dice_type"]}. Ammo: {weapon["ammo"]} \n' for idx, weapon in enumerate(weapons_list)]


def get_characters_move_text(character):
    return f'Ходит {character._name}'


def get_weapon_chosen_text(equipped_weapon_list, weapon_choice):
    return f'Выбрано оружие: {equipped_weapon_list[weapon_choice]["name"]}'


def get_enemy_names_list(enemies_list):
    return [f'{idx}. {enemy._name}: {enemy._hit_points}HP.' for idx, enemy in enumerate(enemies_list)]


def get_enemy_chosen_text(enemies_list, chosen_enemy):
    return f'Для атаки выбран враг: {enemies_list[chosen_enemy]._name}'


def get_target_chosen_text(character_list, chosen_character):
    return f'Для огребания выбран персонаж: {character_list[chosen_character]._name}'


def run_game():
    not_is_over = True
    fight.characters_order.reverse()
    while(not_is_over):
        current_actor = None

        for (character, initiative) in fight.characters_order:
            if character in fight.party.characters:
                print('### Ход персонажа ###')
                print(get_characters_move_text(character))
                current_action = int(input(CHOOSE_ACTION_TEXT))
                if current_action == ACTION_CHOICE:
                    equipped_weapon_list = get_character_weapons_list(
                        character)
                    weapon_choice = int(
                        input(
                            CHOOSE_WEAPON_TEXT +
                            '\n'.join(
                                get_character_weapons_choices_text(
                                    equipped_weapon_list)
                            )
                        )
                    )

                    chosen_weapon = equipped_weapon_list[weapon_choice]

                    print(get_weapon_chosen_text(
                        equipped_weapon_list, weapon_choice))

                    target_chosen = int(
                        input(
                            CHOOSE_TARGET +
                            '\n'.join(get_enemy_names_list(
                                enemies_party.characters))
                        )
                    )

                    chosen_enemy = enemies_party.characters[target_chosen]

                    print(
                        get_enemy_chosen_text(
                            enemies_party.characters,
                            target_chosen,
                        )
                    )

                    damage = character.attack(
                        chosen_enemy,
                        chosen_weapon,
                        get_random_d10()
                    )

                    print(
                        f'Персонаж {character._name} атакует {chosen_enemy._name} из оружия {chosen_weapon["name"]}\n')
                    print(f'{chosen_enemy._name} получает урон {damage}\n' if damage >
                          0 else f'{chosen_enemy._name} уклоняется от атаки\n')

            if character in fight.enemies_party.characters:
                print('### Ход Врага ###')
                equipped_weapon_list = get_character_weapons_list(
                    character)
                weapon_choice = int(randint(0, len(equipped_weapon_list) - 1))
                chosen_weapon = equipped_weapon_list[weapon_choice]

                print(get_weapon_chosen_text(
                    equipped_weapon_list, weapon_choice))

                target_chosen = int(randint(0, len(party.characters) - 1))
                chosen_character = party.characters[target_chosen]

                print(
                    get_target_chosen_text(
                        party.characters,
                        target_chosen,
                    )
                )

                damage = character.attack(
                    chosen_character,
                    chosen_weapon,
                    get_random_d10()
                )

                print(
                    f'Персонаж {character._name} атакует {chosen_character._name} из оружия {chosen_weapon["name"]}\n')
                print(f'{chosen_character._name} получает урон {damage}\n' if damage >
                      0 else f'{chosen_character._name} уклоняется от атаки\n')

        not_is_over = False


run_game()
