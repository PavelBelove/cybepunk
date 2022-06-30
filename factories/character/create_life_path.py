from random import choice, randint


from character_data.life_path_rus import FAMILY, MOTIVATION, GOALS, FRIENDS, ENEMIES, ROMANCE, PERSONALITY, life_path_exemples
from classes.life_path import Family, Motivation, Goals, Friends, Enemies, Romance, Personality


class LifePath():
    def __init__(self, life_path_dict: dict) -> None:
        self.Family = FAMILY[Family[life_path_dict['Family']]]
        self.Motivation = MOTIVATION[Motivation[life_path_dict['Motivation']]]
        self.Goals = GOALS[Goals[life_path_dict['Goals']]]
        self.Friends = []
        self.Enemies = []
        self.Romance = ROMANCE[Romance[life_path_dict['Romance']]]
        self.Personality = PERSONALITY[Personality[life_path_dict['Personality']]]

        for i in life_path_dict['Friends']:
            self.Friends.append(FRIENDS[Friends[i]])

        for i in life_path_dict['Enemies']:
            self.Enemies.append(ENEMIES[Enemies[i]])


class RandomLifePath():
    def __init__(self) -> None:
        self.Family = FAMILY[choice(list(Family))]
        self.Motivation = MOTIVATION[choice(list(Motivation))]
        self.Goals = GOALS[choice(list(Goals))]
        self.Friends = []
        self.Enemies = []
        self.Romance = ROMANCE[choice(list(Romance))]
        self.Personality = PERSONALITY[choice(list(Personality))]

        for i in range(1, randint(1, 11)):
            if i > 7:
                self.Friends.append(FRIENDS[choice(list(Friends))])

        for i in range(1, randint(1, 11)):
            if i > 5:
                self.Enemies.append(ENEMIES[choice(list(Enemies))])


class CreateLifePath():
    def __init__(self) -> None:
        pass

    def create(life_path_dict={}):
        if len(life_path_dict):
            return LifePath(life_path_dict)
        else:
            return RandomLifePath()


# class LifePathDictGenerator():
#     def __init__(self) -> None:
#         self.Family = choice(list(Family)).value[0]
#         self.Motivation = choice(list(Motivation)).value[0]
#         self.Goals = choice(list(Goals)).value[0]
#         self.Friends = []
#         self.Enemies = []
#         self.Romance = choice(list(Romance)).value[0]
#         self.Personality = choice(list(Personality)).value[0]

#         for i in range(1, randint(1, 11)):
#             if i > 7:
#                 self.Friends.append(choice(list(Friends)).value[0])

#         for i in range(1, randint(1, 11)):
#             if i > 5:
#                 self.Enemies.append(choice(list(Enemies)).value[0])


if __name__ == '__main__':
    # lst = []
    # for i in range(20):
    #     test = LifePathDictGenerator()
    #     lst.append(test.__dict__)
    # print(lst)

    test1 = CreateLifePath.create(life_path_exemples[5])
    test2 = CreateLifePath.create()
    print(test1.__dict__)
    print(test2.__dict__)
