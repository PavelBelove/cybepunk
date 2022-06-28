from enum import Enum


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


MOTIVATION = {
    Motivation.d1: 'Деньги',
    Motivation.d2: 'Честь',
    Motivation.d3: 'Данное вами слово',
    Motivation.d4: 'Честность',
    Motivation.d5: 'Знания',
    Motivation.d6: 'Месть',
    Motivation.d7: 'Любовь',
    Motivation.d8: 'Власть',
    Motivation.d9: 'Удовольствие',
    Motivation.d10: 'Дружба'
}

print(MOTIVATION[Motivation.d3])
