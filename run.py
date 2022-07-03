from factories.character.character_factory import CharacterFactory
from factories.stats_factory import StatsFactory
from factories.weapon.melee_weapon_factory import MeleeWeaponFactory
from random_gen.dises import get_random_d10, get_random_d6

print("Welcome to Cyberpunk Terminal")
print("\n")
name = input("Enter your Cyberpunk character name:")

print("Choose your Cyberpunk character class:\n")
print("Available classes are:\n")
print("1. Fixer\n")
print("2. Rockerboy\n")
role_number = input()

stats_factory = StatsFactory()
melee_weapon_factory = MeleeWeaponFactory()
character_factory = CharacterFactory(stats_factory, melee_weapon_factory)

character = character_factory.create_random_fixer(name)
enemy = character_factory.create_random_fixer("mudak")

print(f'{character._name} attacks {enemy._name} with {character._weapon.name}\n')


while(int(enemy._hit_points) > 0):  # TODO: fixme str
    d10_1, d10_2, d6 = get_random_d10(), get_random_d10(), get_random_d6()
    print(f'your dises is {d10_1}, {d10_2}, {d6}')

    damage = character.attack(
        enemy,
        d10_1,
        d10_2,
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
