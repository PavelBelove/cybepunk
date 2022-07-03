from uuid import uuid4

pistol_data = {
    'heavy_pistol': {
        'id': uuid4(),
        'name': 'small_knife',
        'mass': 'light',
        # 'damage': '',
        'hands': 1,
        'price': 10,
        # 'quality': '',
        'is_hidden': True,
        'dices': 3,
        'dice_type': 6,
    },
}

ammo_pistol_data = {
    'ammo_heavy_pistol': {
        'name': '9mm',
        'price': 10,
        'quantity': 15,
    }
}
