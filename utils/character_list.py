
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table
from rich import box
from classes.character.character import Character

from factories.character.character_factory import CharacterFactory
from factories.character.life_path_factory import LifePathFactory
from factories.stats_factory import StatsFactory
from factories.weapon.melee_weapon_factory import MeleeWeaponFactory
from factories.weapon.weapon_factory import WeaponFactory
from factories.weapon.guns_factory import GunFactory
from utils.dises import get_random_d10, get_random_d6


# print('STATS:    ', character._stats.__dict__)
# print('SKILLS:   ', character._skills.__dict__)
# print('LIFE PATH:   ', character._life_path.__dict__)


def character_list(character: Character):
    console = Console()
    name = Panel('[red]' + character._name, style="red",)
    role = Panel(character._role, style="red",)
    hits = Panel(
        f'[red]{character._hit_points}[/red] / [green]{character._max_hit_points}[/green]', style="red",)

    # STATS
    stats = []
    for key, value in character._stats.__dict__.items():
        stats.append(f'{key[1:].capitalize()}: {value} ')

    # Skills
    skills = []
    for key, value in character._skills.__dict__.items():
        skills.append(f'{key[1:].capitalize()}: [cyan bold]{value} ')

    skills_table = Table(title='Skills', show_header=False,
                         width=70, min_width=70, box=box.ROUNDED)
    for i in range(0, 21, 3):
        skills_table.add_row(skills[i], skills[i+1], skills[i+2])

    # Life path
    life_path = []
    for key, value in character._life_path.__dict__.items():
        if type(value) == str:
            life_path.append([key, value])
        elif type(value) == list and len(value) == 0:
            life_path.append([key, 'None'])
        else:
            actors = ''
            for i in value:
                actors += i + '\n'
            life_path.append([key, actors[:-1]])
    # print(life_path)
    console.print(Columns((name, role, hits)))
    console.print(Panel(Columns(stats), style="red",
                        title='[red]STATS', width=70, ))
    console.print(skills_table, style="red")
    for i in life_path:
        console.print(Panel(i[1], style="red", title=i[0], width=70))


if __name__ == '__main__':
    stats_factory = StatsFactory()
    life_path_factory = LifePathFactory()

    melee_weapon_factory = MeleeWeaponFactory()
    gun_factory = GunFactory()
    weapon_factory = WeaponFactory(
        melee_weapon_factory, gun_factory)
    character_factory = CharacterFactory(
        stats_factory, life_path_factory, weapon_factory)

    character = character_factory.create_random_fixer('Hero')

    character_list(character)
