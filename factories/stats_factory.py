from character_data_out.stats.stat_presets import STATS_PRESETS
from classes.character.stats import Stats


class StatsFactory:
    def __init__(self):
        pass

    def _create_preset_stats(self, role, dice_result) -> Stats:
        role_stats_preset = STATS_PRESETS[role][dice_result if dice_result <=
                                                6 else dice_result % 6]
        return Stats(
            intel=role_stats_preset["intelligence"],
            ref=role_stats_preset["reflexes"],
            dex=role_stats_preset["agility"],
            tech=role_stats_preset["tech"],
            cool=role_stats_preset["cool"],
            will=role_stats_preset["will"],
            lusk=role_stats_preset["luck"],
            move=role_stats_preset["movement"],
            body=role_stats_preset["body"],
            emp=role_stats_preset["empathy"]
        )
