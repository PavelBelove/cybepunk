from core.character_data.items.item_options import ITEM_TYPE, IMPLANT_SLOTS, MASS, HANDS


fixer_items = [
    {
        'item_type': ITEM_TYPE['gun'],
        'name': 'Heavy Pistol',
        'weight': MASS['light'],
        'hands': HANDS['one'],
        'in hands': True
        'price': 100,
        'is_hidden': False,
        'dices': 3,
        'dice_type': 6,
        'ammo': 10,
        'max_ammo': 10,
    },
    {
        'item_type': ITEM_TYPE['implanted_weapon'],
        'name': 'Medium SMG',
        'weight': MASS['implant'],
        'hands': HANDS['one'],
        'installed': True,
        'slot': IMPLANT_SLOTS['right_hand'],
        'price': 200,
        'is_hidden': True,
        'dices': 2,
        'dice_type': 6,
    },
    {
        'item_type': ITEM_TYPE['modifier_implants'],
        'name': 'Cyberaudio',
        'weight': MASS['implant'],
        'installed': True,
        'slot': IMPLANT_SLOTS['brain'],
        'price': 250,
        'is_hidden': True,
        'dices': 2,
        'dice_type': 6,
    },
    {
        'item_type': ITEM_TYPE['modifier_implants'],
        'name': 'Cyberoptics Low Light',
        'weight': MASS['implant'],
        'installed': True,
        'slot': IMPLANT_SLOTS['right_eye'],
        'price': 250,
        'is_hidden': True,
        'dices': 2,
        'dice_type': 6,
    },
    {
        'item_type': ITEM_TYPE['coins'],
        'name': 'Coins',
        'weight': MASS['light'],
        'price': 100,
        'is_hidden': True,
    },
    {
        'item_type': ITEM_TYPE['electronics'],
        'name': 'Agent',
        'weight': MASS['light'],
        'price': 100,
        'is_hidden': True,
    },

]
