from random import choice, randint
import json
from rich import print


from character.character_data.stats.stat_presets import STATS_PRESETS
# from character_data.stats.stat_presets import STATS_PRESETS


def preset_stats(role_presets, dispersion=0):
    '''
    Выдает случайные статы из пресета согласно роли.
    dispersion - случайные отклонения от пресета 
    Значения более 10 и менее 3 заменяются 10 и 3 соответственно
    '''

    def modified_stat(stat, dispersion=dispersion):
        '''Случайные отклонения'''
        modified_stat = stat + randint(-dispersion, dispersion)
        if modified_stat > 10:
            return 10
        elif modified_stat < 3:
            return 3
        return modified_stat

    preset = role_presets[choice(list(role_presets))]

    stats = {
        'intel': modified_stat(preset['intelligence']),
        'ref': modified_stat(preset['reflexes']),
        'dex': modified_stat(preset['agility']),
        'tech': modified_stat(preset['tech']),
        'cool': modified_stat(preset['cool']),
        'will': modified_stat(preset['will']),
        'lusk': modified_stat(preset['luck']),
        'move': modified_stat(preset['movement']),
        'body': modified_stat(preset['body']),
        'emp': modified_stat(preset['empathy']),
    }

    print(preset)
    return json.dumps(stats)


if __name__ == '__main__':
    print(preset_stats(STATS_PRESETS['FIXER'], 0))
