from core.classes.items.armor import Armor
from core.character_data.armor_presets import ARMOR_PRESETS


class ArmorFactory():
    def __init__(self) -> None:
        pass

    def create_armor(self, armor_data):
        return Armor(**armor_data)
