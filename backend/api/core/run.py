from rich import print

from factories.character.character_factory import CharacterFactory
from factories.character.life_path_factory import LifePathFactory
from factories.stats_factory import StatsFactory
from factories.weapon.melee_weapon_factory import MeleeWeaponFactory
from factories.weapon.weapon_factory import WeaponFactory
from factories.weapon.guns_factory import GunFactory
from utils.dises import get_random_d10, get_random_d6
from utils.character_list import character_list

print("Welcome to Cyberpunk Terminal")
print("\n")
name = input("Enter your Cyberpunk character name:")
# name = 'SuperHero'

print("Choose your Cyberpunk character class:\n")
print("Available classes are:\n")
print("1. Fixer\n")
print("2. Rockerboy\n")
role_number = input()
# role_number = '1'

stats_factory = StatsFactory()
life_path_factory = LifePathFactory()
melee_weapon_factory = MeleeWeaponFactory()
gun_factory = GunFactory()
weapon_factory = WeaponFactory(melee_weapon_factory, gun_factory)
character_factory = CharacterFactory(
    stats_factory, life_path_factory, weapon_factory)

character = character_factory.create_random_fixer(name)
enemy = character_factory.create_random_fixer("mudak")

character_list(character)

# character.set_weapon

print(f'{character._name} attacks {enemy._name} with {character._right_hand_weapon.name}\n')

# print(character.set_weapon(weapon_factory.create_fixer_weapons()))

while(int(enemy._hit_points) > 0):  # TODO: fixme str
    d6 = get_random_d6()
    print(f'your dises is {d10_1}, {d10_2}, {d6}')

    damage = character.attack(
        enemy,
        character._right_hand_weapon,
        d6
    )
    if (damage > 0):
        print(f'{enemy._name} {"getting damage " + str(damage)}')
        print(f'{enemy._name} remaining health is {int(enemy._hit_points) - damage}')
        enemy._hit_points = str(int(enemy._hit_points) - damage)

        if (int(enemy._hit_points) <= 0):
            print(f'pizdeath')
    else:
        print("evading the attack")

input("Try again (press Enter):")
