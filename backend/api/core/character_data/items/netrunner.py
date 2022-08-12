from core.character_data.items.item_options import ITEM_TYPE, IMPLANT_SLOTS, MASS, HANDS


netrunner_items = [
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
        'item_type': ITEM_TYPE['modifier_implants'],
        'name': 'Interface Plugs',
        'weight': MASS['implant'],
        'installed': True,
        'slot': IMPLANT_SLOTS['brain'],
        'price': 250,
        'is_hidden': True,
    },
    {
        'item_type': ITEM_TYPE['electronics'],
        'name': 'Agent',
        'weight': MASS['light'],
        'price': 100,
        'is_hidden': True,
    },
    {
        'item_type': ITEM_TYPE['electronics'],
        'name': 'Cyberdeck & Cables',
        'weight': MASS['light'],
        'price': 500,
        'is_hidden': True,
    },
    {
        'item_type': ITEM_TYPE['programs'],
        'name': 'Speedy Gonzalvez',
        'weight': MASS['implant'],
        'price': 250,
        'is_hidden': True,
        'dices': 2,
        'dice_type': 6,
    },
    {
        'item_type': ITEM_TYPE['programs'],
        'name': 'Banhammer',
        'weight': MASS['implant'],
        'price': 250,
        'is_hidden': True,
        'dices': 2,
        'dice_type': 6,
    },
    {
        'item_type': ITEM_TYPE['programs'],
        'name': 'Flack',
        'weight': MASS['implant'],
        'price': 250,
        'is_hidden': True,
        'dices': 2,
        'dice_type': 6,
    },
    {
        'item_type': ITEM_TYPE['programs'],
        'name': 'Black ICE Hellhound',
        'weight': MASS['implant'],
        'price': 250,
        'is_hidden': True,
        'dices': 5,
        'dice_type': 6,
    },


]
