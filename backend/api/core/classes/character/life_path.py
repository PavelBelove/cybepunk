from random import choice, randint

from core.character_data.life_path_rus import FAMILY, MOTIVATION, GOALS, FRIENDS, ENEMIES, ROMANCE, PERSONALITY, life_path_exemples
from core.classes.character.life_path_enums import Family, Motivation, Goals, Friends, Enemies, Romance, Personality


class LifePath():
    def __init__(self) -> None:
        pass


class PresetLifePath(LifePath):
    def __init__(self, life_path_dict: dict) -> None:
        self.family = FAMILY[Family[life_path_dict['Family']]]
        self.motivation = MOTIVATION[Motivation[life_path_dict['Motivation']]]
        self.goals = GOALS[Goals[life_path_dict['Goals']]]
        self.friends = []
        self.enemies = []
        self.romance = ROMANCE[Romance[life_path_dict['Romance']]]
        self.personality = PERSONALITY[Personality[life_path_dict['Personality']]]

        for i in life_path_dict['Friends']:
            self.friends.append(FRIENDS[Friends[i]])

        for i in life_path_dict['Enemies']:
            self.enemies.append(ENEMIES[Enemies[i]])

        def as_json(self):
            return {
                'Family': self.family,
                'Motivation': self.motivation,
                'Goals': self.goals,
                'Friends': self.friends,
                'Enemies': self.enemies,
                'Romance': self.romance,
                'Personality': self.personality,
            }


class RandomLifePath(LifePath):
    def __init__(self) -> None:
        self.family = FAMILY[choice(list(Family))]
        self.motivation = MOTIVATION[choice(list(Motivation))]
        self.goals = GOALS[choice(list(Goals))]
        self.friends = []
        self.enemies = []
        self.romance = ROMANCE[choice(list(Romance))]
        self.personality = PERSONALITY[choice(list(Personality))]

        for i in range(1, randint(1, 11)):
            if i > 7:
                self.friends.append(FRIENDS[choice(list(Friends))])

        for i in range(1, randint(1, 11)):
            if i > 5:
                self.enemies.append(ENEMIES[choice(list(Enemies))])

    def as_json(self):
        return {
            'family': self.family,
            'motivation': self.motivation,
            'goals': self.goals,
            'friends': self.friends,
            'enemies': self.enemies,
            'romance': self.romance,
            'personality': self.personality,
        }


# class LifePathDictGenerator():
#     def __init__(self) -> None:
#         self.family = choice(list(Family)).value[0]
#         self.motivation = choice(list(Motivation)).value[0]
#         self.goals = choice(list(Goals)).value[0]
#         self.friends = []
#         self.enemies = []
#         self.romance = choice(list(Romance)).value[0]
#         self.personality = choice(list(Personality)).value[0]

#         for i in range(1, randint(1, 11)):
#             if i > 7:
#                 self.friends.append(choice(list(Friends)).value[0])

#         for i in range(1, randint(1, 11)):
#             if i > 5:
#                 self.enemies.append(choice(list(Enemies)).value[0])
