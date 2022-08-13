from core.character_data.items.item_options import ITEM_TYPE, IMPLANT_SLOTS, MASS, HANDS


rocker_items = [
    {
        'item_type': ITEM_TYPE['gun'],
        'name': 'Very Heavy Pistol',
        'weight': MASS['medium'],
        'hands': HANDS['one'],
        'in_hands': True,
        'price': 100,
        'is_hidden': False,
        'dices': 4,
        'dice_type': 6,
        'ammo': 10,
        'max_ammo': 10,
    },
    {
        'item_type': ITEM_TYPE['implanted_weapon'],
        'name': 'Slice & Dice',
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
    },
    {
        'item_type': ITEM_TYPE['subject'],
        'name': 'guitar',
        'weight': MASS['light'],
        'price': 300,
        'is_hidden': False,
    },
    {
        'item_type': ITEM_TYPE['electronics'],
        'name': 'Agent',
        'weight': MASS['light'],
        'price': 100,
        'is_hidden': True,
    },
]
