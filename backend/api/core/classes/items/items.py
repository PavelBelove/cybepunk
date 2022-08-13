from enum import Enum
import uuid


class Weight(Enum):
    implant = 0
    light = 1
    medium = 2
    heavy = 3


class Item():
    def __init__(
        self,
        name=None,
        item_type=None,
        weight=None,
        price=None,
        installed=None,
        slot=None,
        humanity_penalty=None,
        skill_modifier=None,
        hands=None,
        in_hands=None,
        is_hidden=None,
        dices=None,
        dice_type=None,
        ammo=None,
        max_ammo=None,
    ):
        self.uuid = uuid.uuid4()
        self.name = name
        self.item_type = item_type
        self.weight = weight
        self.price = price
        self.installed = installed
        self.slot = slot
        self.humanity_penalty = humanity_penalty
        self.skill_modifier = skill_modifier
        self.hands = hands
        self.in_hands = in_hands
        self.is_hidden = is_hidden
        self.dices = dices
        self.dice_type = dice_type
        self.ammo = ammo
        self.max_ammo = max_ammo
