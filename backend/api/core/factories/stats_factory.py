from random import choice, randint

from core.character_data.stats.stat_presets import STATS_PRESETS
from core.classes.character.stats import Stats


class StatsFactory:
    def __init__(self):
        pass

#     def _create_preset_stats(self, role, dice_result) -> Stats:
#         role_stats_preset = STATS_PRESETS[role][dice_result if dice_result <=
#                                                 6 else dice_result % 6]
#         return Stats(
#             intel=role_stats_preset["intelligence"],
#             ref=role_stats_preset["reflexes"],
#             dex=role_stats_preset["agility"],
#             tech=role_stats_preset["tech"],
#             cool=role_stats_preset["cool"],
#             will=role_stats_preset["will"],
#             lusk=role_stats_preset["luck"],
#             move=role_stats_preset["movement"],
#             body=role_stats_preset["body"],
#             emp=role_stats_preset["empathy"]
#         )

    def _create_preset_stats(self, role, dispersion=0):
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

        preset = STATS_PRESETS[role][choice(list(STATS_PRESETS[role]))]

        return Stats(
            intel=modified_stat(preset['intelligence']),
            ref=modified_stat(preset['reflexes']),
            dex=modified_stat(preset['agility']),
            tech=modified_stat(preset['tech']),
            cool=modified_stat(preset['cool']),
            will=modified_stat(preset['will']),
            lusk=modified_stat(preset['luck']),
            move=modified_stat(preset['movement']),
            body=modified_stat(preset['body']),
            emp=modified_stat(preset['empathy']),
        )
