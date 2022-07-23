from enum import Enum


class Family(Enum):
    d1 = 'd1',
    d2 = 'd2',
    d3 = 'd3',
    d4 = 'd4',
    d5 = 'd5',
    d6 = 'd6',
    d7 = 'd7',
    d8 = 'd8',
    d9 = 'd9',
    d10 = 'd10'


class Motivation(Enum):
    d1 = 'd1',
    d2 = 'd2',
    d3 = 'd3',
    d4 = 'd4',
    d5 = 'd5',
    d6 = 'd6',
    d7 = 'd7',
    d8 = 'd8',
    d9 = 'd9',
    d10 = 'd10'


class Goals(Enum):
    d1 = 'd1',
    d2 = 'd2',
    d3 = 'd3',
    d4 = 'd4',
    d5 = 'd5',
    d6 = 'd6',
    d7 = 'd7',
    d8 = 'd8',
    d9 = 'd9',
    d10 = 'd10'


class Friends(Enum):
    d1 = 'd1',
    d2 = 'd2',
    d3 = 'd3',
    d4 = 'd4',
    d5 = 'd5',
    d6 = 'd6',
    d7 = 'd7',
    d8 = 'd8',
    d9 = 'd9',
    d10 = 'd10'


class Enemies(Enum):
    d1 = 'd1',
    d2 = 'd2',
    d3 = 'd3',
    d4 = 'd4',
    d5 = 'd5',
    d6 = 'd6',
    d7 = 'd7',
    d8 = 'd8',
    d9 = 'd9',
    d10 = 'd10'


class Romance(Enum):
    d1 = 'd1',
    d2 = 'd2',
    d3 = 'd3',
    d4 = 'd4',
    d5 = 'd5',
    d6 = 'd6',
    d7 = 'd7',
    d8 = 'd8',
    d9 = 'd9',
    d10 = 'd10'


class Personality(Enum):
    d1 = 'd1',
    d2 = 'd2',
    d3 = 'd3',
    d4 = 'd4',
    d5 = 'd5',
    d6 = 'd6',
    d7 = 'd7',
    d8 = 'd8',
    d9 = 'd9',
    d10 = 'd10'


class LifePath():
    def __init__(
        self,
        family=None,
        motivation=None,
        goals=None,
        friends=[],
        enemies=[],
        romanse=None,
        personality=None,
    ) -> None:
        self.family = family
        self.motivation = motivation
        self.goals = goals
        self.friends = friends
        self.enemies = enemies
        self.romanse = romanse
        self.personality = personality

    def set_life_path(life_path):
        pass

    def generate_random_life_path():
        pass
