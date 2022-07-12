from classes.character.life_path import LifePath, PresetLifePath, RandomLifePath
from character_data.life_path_rus import life_path_exemples


class LifePathFactory():
    def __init__(self) -> None:
        pass

    def create(self, life_path_dict={}):
        if len(life_path_dict):
            return PresetLifePath(life_path_dict)
        else:
            return RandomLifePath()


if __name__ == '__main__':
    # lst = []
    # for i in range(20):
    #     test = LifePathDictGenerator()
    #     lst.append(test.__dict__)
    # print(lst)

    life_path_factory = LifePathFactory()
    test1 = life_path_factory.create(life_path_exemples[0])
    test2 = life_path_factory.create()
    print(test1.__dict__)
    print(isinstance(test2, LifePath))
