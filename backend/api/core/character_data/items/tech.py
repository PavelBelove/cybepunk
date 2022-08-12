from core.character_data.items.item_options import ITEM_TYPE, IMPLANT_SLOTS, MASS, HANDS


tech_items = [
    {
        'item_type': ITEM_TYPE['gun'],
        'name': 'Heavy Pistol',
        'weight': MASS['light'],
        'hands': HANDS['one'],
        'price': 100,
        'is_hidden': False,
        'dices': 3,
        'dice_type': 6,
        'ammo': 10,
        'max_ammo': 10,
    },
    {
        'item_type': ITEM_TYPE['gun'],
        'name': 'Shotgun',
        'weight': MASS['heavy'],
        'hands': HANDS['two'],
        'price': 300,
        'is_hidden': False,
        'dices': 5,
        'dice_type': 6,
        'ammo': 5,
        'max_ammo': 5,
    },
    {
        'item_type': ITEM_TYPE['implanted_weapon'],
        'name': 'Cyberarm',
        'weight': MASS['implant'],
        'installed': True,
        'slot': IMPLANT_SLOTS['right_hand'],
        'price': 500,
        'is_hidden': True,
        'dices': 1,
        'dice_type': 6,
    },
    {
        'item_type': ITEM_TYPE['implanted_weapon'],
        'name': 'Big Knucks',
        'weight': MASS['implant'],
        'hands': HANDS['one'],
        'installed': True,
        'slot': IMPLANT_SLOTS['left_hand'],
        'price': 200,
        'is_hidden': True,
        'dices': 2,
        'dice_type': 6,
    },
    {
        'item_type': ITEM_TYPE['modifier_implants'],
        'name': 'Cyberoptics Camera',
        'weight': MASS['implant'],
        'installed': True,
        'slot': IMPLANT_SLOTS['right_eye'],
        'price': 250,
        'is_hidden': True,
    },
    {
        'item_type': ITEM_TYPE['subject'],
        'name': 'Technical Tool Box & Tools',
        'weight': MASS['light'],
        'price': 300,
        'is_hidden': False,
    },
]